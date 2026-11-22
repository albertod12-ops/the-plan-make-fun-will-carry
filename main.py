"""the-plan-make-fun-will-carry - v2.

Competition: the-plan-make-fun-will-carry-20261122-2138 (program/v1).
Writes a 30-day plan for an AI agent to turn $100 into as much money as
possible, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, deterministic, no network. v2 plan: 274 chars.

Changes vs v1: adds a $29/mo upkeep retainer and "One script serves all"
(near-zero marginal cost per new client), tightens the offer wording.
"""

import os

PLAN = "Day 1: list 300 US plumbers on Google Maps with no online booking; email owners a $99 AI missed-call textback + reviews (Twilio, their keys), $29/mo upkeep. One script serves all. $100: Twilio + Apollo. Close 4-6; target $400-600 by day 30. No replies by day 7: halve price."


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
