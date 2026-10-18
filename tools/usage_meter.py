#!/usr/bin/env python3
"""Estimate session usage burn from Claude Code transcripts, to pace agents under a usage limit.

    python3 tools/usage_meter.py                 # burn since the window start, last 10/30 min, by model
    python3 tools/usage_meter.py --minutes 15    # also show the rate over the last 15 minutes

Cost units weight token types like API pricing (cache write 1.25x input, cache read 0.1x,
output 5x) and models by a relative multiplier (Opus = 1). The calibration point maps
units to % of the window: the user reported 30% used at 23:46 UTC for the window that
reset at 23:30 UTC on 2026-10-17. Re-calibrate with --calibrate PCT AT_ISO when the
user reports a new reading.
"""
import argparse
import glob
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta, timezone

SESSION_DIR = os.path.expanduser(
    "~/.claude/projects/-home-user-quant-credit-book/6416563a-50d0-5129-a66c-5b16ba7386c8")
CAL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "state", "usage_calibration.json")
TYPE_W = {"input_tokens": 1.0, "cache_creation_input_tokens": 1.25, "cache_read_input_tokens": 0.1, "output_tokens": 5.0}
MODEL_W = {"opus": 1.0, "fable": 2.0, "sonnet": 0.6, "haiku": 0.2}  # rough relative price; the calibration absorbs the level


def model_weight(model):
    for k, w in MODEL_W.items():
        if k in (model or ""):
            return w
    return 1.0


def records():
    files = glob.glob(os.path.join(SESSION_DIR, "**", "*.jsonl"), recursive=True)
    files += glob.glob(SESSION_DIR + ".jsonl")
    seen = set()
    for f in files:
        try:
            for line in open(f, encoding="utf-8"):
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                msg = d.get("message") if isinstance(d.get("message"), dict) else {}
                u = msg.get("usage")
                rid = d.get("requestId") or d.get("uuid")
                if not u or not d.get("timestamp") or rid in seen:
                    continue
                seen.add(rid)
                ts = datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00"))
                units = sum(TYPE_W[k] * (u.get(k) or 0) for k in TYPE_W) * model_weight(msg.get("model"))
                yield ts, msg.get("model", "?"), units
        except OSError:
            continue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--window-start", default=None, help="ISO time the usage window began")
    ap.add_argument("--minutes", type=int, default=10)
    ap.add_argument("--calibrate", nargs=2, metavar=("PCT", "AT_ISO"))
    args = ap.parse_args()

    cal = {"window_start": "2026-10-17T23:30:00+00:00", "pct": 30.0, "at": "2026-10-17T23:46:00+00:00",
           "window_hours": 5}
    if os.path.exists(CAL_FILE):
        cal.update(json.load(open(CAL_FILE)))
    if args.window_start:
        cal["window_start"] = args.window_start
    if args.calibrate:
        cal["pct"], cal["at"] = float(args.calibrate[0]), args.calibrate[1]
        json.dump(cal, open(CAL_FILE, "w"), indent=2)

    start = datetime.fromisoformat(cal["window_start"])
    at = datetime.fromisoformat(cal["at"])
    now = datetime.now(timezone.utc)
    recs = [r for r in records() if r[0] >= start]
    total = sum(u for t, _, u in recs)
    at_units = sum(u for t, _, u in recs if t <= at)
    if at >= start and at_units:
        units_per_pct = at_units / cal["pct"]
        if abs(cal.get("units_per_pct", 0) - units_per_pct) > 1e-9:
            cal["units_per_pct"] = units_per_pct  # carried into the next window until the user gives a new reading
            json.dump(cal, open(CAL_FILE, "w"), indent=2)
    else:
        units_per_pct = cal.get("units_per_pct", float("nan"))  # calibration predates this window: reuse the last scale

    def window(mins):
        return sum(u for t, _, u in recs if t >= now - timedelta(minutes=mins))

    by_model = defaultdict(float)
    for t, m, u in recs:
        if t >= now - timedelta(minutes=args.minutes):
            by_model[m] += u
    used_pct = total / units_per_pct
    end = start + timedelta(hours=cal["window_hours"])
    mins_left = max(1.0, (end - now).total_seconds() / 60)
    rate = window(args.minutes) / args.minutes / units_per_pct  # % per minute
    print(f"window {start:%H:%M}–{end:%H:%M} UTC  now {now:%H:%M}  minutes left {mins_left:.0f}")
    print(f"estimated used: {used_pct:5.1f}%   (calibration: {cal['pct']}% at {at:%Y-%m-%d %H:%M}{'' if at >= start else ', scale carried from the previous window'})")
    print(f"burn over last {args.minutes} min: {rate:.2f}%/min  -> projected at window end: {used_pct + rate * mins_left:5.1f}%")
    print(f"sustainable rate to finish at 90%: {(90 - used_pct) / mins_left:.2f}%/min")
    for m, u in sorted(by_model.items(), key=lambda x: -x[1]):
        print(f"  {m:<24} {u / units_per_pct / args.minutes:.3f}%/min")


if __name__ == "__main__":
    main()
