#!/usr/bin/env python3
"""
Solution to the Rope Folding problem.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    L = int(next(it))
    # Read knot positions
    knots = [int(next(it)) for _ in range(N)]
    knot_set = set(knots)
    # Use doubled fold position f2 = xi + xj for candidates
    two_L = 2 * L
    seen = set()
    valid_count = 0
    # Enumerate fold candidates (as f2 = 2*f)
    for i in range(N):
        for j in range(i, N):
            f2 = knots[i] + knots[j]
            # fold point f = f2/2 must satisfy 0 < f < L => 0 < f2 < 2L
            if f2 <= 0 or f2 >= two_L:
                continue
            if f2 in seen:
                continue
            seen.add(f2)
            # overlapping region half-length doubled
            d2 = min(f2, two_L - f2)
            # check symmetry in overlapping region
            valid = True
            for x in knots:
                # if knot x lies within overlapping region
                if abs(2 * x - f2) <= d2:
                    # mirrored position
                    x_mirror = f2 - x
                    if x_mirror not in knot_set:
                        valid = False
                        break
            if valid:
                valid_count += 1
    # Output result
    print(valid_count)

if __name__ == '__main__':
    main()
