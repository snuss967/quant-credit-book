#!/usr/bin/env python3
"""Background pacing guard: exits (waking the orchestrator) only when pacing needs a decision.

    python3 tools/pace_guard.py [--target 88] [--slack 0.6] [--check-every 180]

Exit reasons (one line printed, then exit):
  TOO_FAST   projected end-of-window usage exceeds --target %   -> shed agents
  SLACK      rate is below --slack x sustainable for 20 minutes  -> add agents
  NEAR_CAP   used >= target - 6                                  -> pause launches, finish in-flight work
"""
import argparse
import re
import subprocess
import sys
import time

METER = [sys.executable, "tools/usage_meter.py", "--minutes", "10"]


def reading():
    out = subprocess.run(METER, capture_output=True, text=True).stdout
    used = float(re.search(r"estimated used:\s+([\d.]+)%", out).group(1))
    rate = float(re.search(r"burn over last 10 min: ([\d.]+)%/min", out).group(1))
    left = float(re.search(r"minutes left (\d+)", out).group(1))
    return used, rate, left, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=float, default=88.0)
    ap.add_argument("--slack", type=float, default=0.6)
    ap.add_argument("--check-every", type=int, default=180)
    ap.add_argument("--cap-only", action="store_true", help="alert only at NEAR_CAP (throughput mode)")
    ap.add_argument("--settle", type=int, default=600)
    args = ap.parse_args()
    time.sleep(args.settle)  # let the current mix settle before judging it
    slack_since = None
    while True:
        used, rate, left, out = reading()
        sustainable = max(0.0, (args.target - used) / max(left, 1))
        projected = used + rate * left
        if used >= args.target - 6:
            print(f"NEAR_CAP used={used:.1f}% rate={rate:.2f}%/min left={left:.0f}min\n{out}")
            return
        if args.cap_only:
            time.sleep(args.check_every)
            continue
        if projected > args.target + 4 and rate > 1.3 * sustainable:
            print(f"TOO_FAST used={used:.1f}% rate={rate:.2f}%/min sustainable={sustainable:.2f}%/min projected={projected:.0f}%\n{out}")
            return
        if rate < args.slack * sustainable:
            slack_since = slack_since or time.time()
            if time.time() - slack_since > 1200:
                print(f"SLACK used={used:.1f}% rate={rate:.2f}%/min sustainable={sustainable:.2f}%/min\n{out}")
                return
        else:
            slack_since = None
        time.sleep(args.check_every)


if __name__ == "__main__":
    main()
