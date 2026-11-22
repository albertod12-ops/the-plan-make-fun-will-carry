"""30-day plan: turn $100 into as much money as possible.

Competition: the-plan-make-fun-will-carry-20261122-2138 (program/v1).
Writes the plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, stdlib only, deterministic, no network.

The plan: list 200 US HVAC firms on Google Maps with unanswered 1-2
star reviews, then email each owner screenshots of their own lost
reviews plus an offer: a $199 AI missed-call textback (Twilio, their
keys), $49/mo. Close 3-4 of them. The $100 goes to Twilio + Apollo.
Target: $700-900 by day 30. No replies by day 7: halve setup, switch.

Why HVAC: a missed night call is a $300-800 emergency job lost, so
the owner feels the value at once; this is not a nice-to-have tool.
Why proof-first outreach: a generic offer is ignored, but a screenshot
of the owner's own unanswered bad review proves the money lost.
The math: 200 firms, 3-4 closes. Setup $199 x 3-4 = $597-796, plus
first-month retainers $49 x 3-4 = $147-196, for $700-900 by day 30.
The pivot rule: no replies by day 7 means the price or the niche is
wrong, so halve the setup fee and switch to the next trade.

Hard rule (learned from a v2 run_completes rejection): NEVER chmod the
output directory - the grader runs as uid 65534, not the dir owner.
Only chmod the file this program itself creates (0644 below).
"""

import os

PLAN = "Day 1: list 200 US HVAC firms on Google Maps with unanswered 1-2\u2605 reviews; email owners 3 lost-review screenshots + a $199 AI missed-call textback (Twilio, their keys), $49/mo. Close 3-4; $100: Twilio + Apollo. Target $700-900 by day 30. No replies by day 7: halve setup, switch."


def main():
    assert 1 <= len(PLAN) <= 280, f"plan length {len(PLAN)} out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = PLAN.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Only chmod the file this program just created; never the output directory.
    os.chmod(path, 0o644)
    print(f"chars={len(PLAN)} bytes={len(data)} path={path}")


if __name__ == "__main__":
    main()
