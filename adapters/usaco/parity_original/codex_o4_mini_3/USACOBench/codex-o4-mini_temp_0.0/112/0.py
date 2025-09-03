#!/usr/bin/env python3
"""
Rope Folding Problem:
Given a rope of length L with knots at distinct integer positions (including 0 and L),
count integer fold positions f (0 < f < L) where folding back on itself aligns all knots
in the overlapping segment. Extra knots outside overlap on the longer side are allowed.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    L = int(next(it))
    knots = [int(next(it)) for _ in range(n)]
    knot_set = set(knots)
    count = 0
    # Check each integer fold position f
    for f in range(1, L):
        # overlapping segment length
        d = min(f, L - f)
        ok = True
        # For any knot within overlap, check its mirror exists
        for k in knots:
            if abs(k - f) <= d:
                m = 2 * f - k
                if m not in knot_set:
                    ok = False
                    break
        if ok:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
