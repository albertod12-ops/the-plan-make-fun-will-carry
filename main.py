"""the-plan-make-fun-will-carry - v1.

Competition: the-plan-make-fun-will-carry-20261122-2138 (program/v1).
Writes a 30-day plan for an AI agent to turn $100 into as much money as
possible, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, deterministic, no network. v1 plan: 275 chars.
"""

import os

PLAN = "Day 1: list 300 US plumbers off Google Maps with no online booking; email owners a $99 AI missed-call text-back + review replies on Twilio (their keys). $100: Twilio credits + Apollo trial. Close 4-6; target $400-600 by day 30. No replies by day 7: halve price, switch niche."


def main():
    assert 1 <= len(PLAN) <= 280, f"plan length {len(PLAN)} out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    data = PLAN.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    print(f"chars={len(PLAN)} bytes={len(data)} path={path}")


if __name__ == "__main__":
    main()
