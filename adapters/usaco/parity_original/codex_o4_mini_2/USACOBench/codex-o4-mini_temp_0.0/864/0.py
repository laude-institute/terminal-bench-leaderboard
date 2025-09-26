#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    f = [0] * (n + 2)
    for i in range(1, n+1):
        try:
            f[i] = int(next(it))
        except StopIteration:
            f[i] = 0
    # build points
    pts = [(0, 0)] + [(i, f[i]) for i in range(1, n+1)] + [(n+1, 0)]
    # upper concave hull monotone chain
    hull = []  # list of (x,y)
    for p in pts:
        # pop while last turn makes slope non-decreasing
        while len(hull) >= 2:
            x0, y0 = hull[-2]
            x1, y1 = hull[-1]
            x2, y2 = p
            # slope(h0,h1) <= slope(h1,h2)? pop h1
            if (y1 - y0) * (x2 - x1) <= (y2 - y1) * (x1 - x0):
                hull.pop()
            else:
                break
        hull.append(p)
    # compute answers
    ans = [0] * (n + 2)
    # for each segment
    for i in range(len(hull) - 1):
        x1, y1 = hull[i]
        x2, y2 = hull[i+1]
        dx = x2 - x1
        # k from x1 to x2 inclusive, but we only care 1..n
        lo = max(1, x1)
        hi = min(n, x2)
        # precompute multipliers
        for k in range(lo, hi+1):
            # linear interpolation numerator
            num = y1 * (x2 - k) + y2 * (k - x1)
            # g[k] = num/dx
            ans[k] = (num * 100000) // dx
    out = sys.stdout
    for i in range(1, n+1):
        out.write(str(ans[i]))
        out.write("\n")

if __name__ == '__main__':
    main()
