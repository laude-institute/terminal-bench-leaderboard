#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Read payments, pad boundaries with zero
    f = [0] * (N + 2)
    for i in range(1, N + 1):
        f[i] = int(input())
    # Build concave envelope (upper hull) of points (i, f[i])
    hull = []  # list of (x, y)
    for x in range(N + 2):
        y = f[x]
        # Maintain slopes non-increasing
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            # If slope((x1,y1)->(x2,y2)) < slope((x2,y2)->(x,y)), pop last
            if (y2 - y1) * (x - x2) < (y - y2) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append((x, y))
    # Compute expected values via linear interpolation on each segment
    ans = [0] * (N + 2)
    for i in range(len(hull) - 1):
        x0, y0 = hull[i]
        x1, y1 = hull[i + 1]
        dx = x1 - x0
        # fill for k in [x0..x1]
        start = max(1, x0)
        end = min(N, x1)
        for k in range(start, end + 1):
            # numerator for interpolation at k
            num = y0 * (x1 - k) + y1 * (k - x0)
            ans[k] = num * 100000 // dx
    # Output results
    out = sys.stdout.write
    for i in range(1, N + 1):
        out(str(ans[i]) + '\n')

if __name__ == '__main__':
    main()
