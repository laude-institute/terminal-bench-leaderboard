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
        f[i] = int(next(it))

    # Build points for upper hull: (x, f[x]) for x=0..n+1
    pts = [(i, f[i]) for i in range(n+2)]
    # Compute upper convex hull (concave envelope)
    hull = []  # list of (x, y)
    for x, y in pts:
        # Maintain slopes decreasing: remove last while slope(prev, last) < slope(last, new)
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            # compare (y2-y1)/(x2-x1) < (y-y2)/(x-x2)
            if (y2 - y1) * (x - x2) < (y - y2) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append((x, y))

    # Prepare answer array
    res = [0] * (n + 2)
    # For each segment in hull, interpolate
    for i in range(len(hull) - 1):
        x1, y1 = hull[i]
        x2, y2 = hull[i+1]
        dx = x2 - x1
        # compute for x from x1 to x2
        for t in range(0, dx+1):
            x = x1 + t
            if 0 <= x <= n:
                # numerator = y1*(dx - t) + y2*t
                num = y1 * (dx - t) + y2 * t
                # floor of (num/dx)*100000 = num*100000//dx
                res[x] = (num * 100000) // dx

    # Output results for positions 1..n
    out = sys.stdout
    for i in range(1, n+1):
        out.write(str(res[i]))
        out.write("\n")

if __name__ == '__main__':
    main()
