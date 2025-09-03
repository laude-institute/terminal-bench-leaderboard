#!/usr/bin/env python3
"""
Solution for the moo particle interaction problem.
Computes the minimum number of particles remaining, which equals
the size of the largest antichain in 2D, i.e., longest decreasing
subsequence in y after sorting by x then y.
"""
import sys

def main():
    import sys, bisect
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    pts = []
    for _ in range(n):
        x = int(next(it)); y = int(next(it))
        pts.append((x, y))
    # Sort by x ascending, then y ascending
    pts.sort(key=lambda p: (p[0], p[1]))
    # Compute longest decreasing subsequence in y => LIS on -y
    d = []  # tails for LIS on -y
    for _, y in pts:
        v = -y
        # find insertion point for v in d
        pos = bisect.bisect_left(d, v)
        if pos == len(d):
            d.append(v)
        else:
            d[pos] = v
    # result is length of d
    sys.stdout.write(str(len(d)))

if __name__ == '__main__':
    main()
