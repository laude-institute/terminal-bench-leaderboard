#!/usr/bin/env python3
import sys

def can_cover(points, k):
    # Base cases
    if not points:
        return True
    if k == 0:
        return False
    # Pick first point
    x0, y0 = points[0]
    # Try vertical line x = x0
    rem = [p for p in points if p[0] != x0]
    if can_cover(rem, k-1):
        return True
    # Try horizontal line y = y0
    rem = [p for p in points if p[1] != y0]
    if can_cover(rem, k-1):
        return True
    return False

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = []
    idx = 1
    for i in range(n):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        pts.append((x, y))
    result = 1 if can_cover(pts, 3) else 0
    print(result)

if __name__ == '__main__':
    main()
