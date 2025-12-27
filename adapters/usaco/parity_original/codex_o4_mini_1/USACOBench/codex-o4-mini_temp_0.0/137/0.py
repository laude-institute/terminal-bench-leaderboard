#!/usr/bin/env python3
"""
Read input for USACO 'Tied Down' problem, determine how many fence posts
are enclosed by the rope polygon using point-in-polygon test.
"""
import sys

def point_in_polygon(px, py, poly):
    """
    Determine if point (px,py) is inside the polygon defined by poly (list of (x,y)).
    Uses ray casting to the right; returns True if inside (odd crossings).
    """
    cnt = 0
    n = len(poly)
    for i in range(n - 1):
        x1, y1 = poly[i]
        x2, y2 = poly[i+1]
        # Check if edge crosses horizontal ray at y=py
        if (y1 > py) != (y2 > py):
            # Compute x coordinate of intersection
            x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x_int > px:
                cnt += 1
    return (cnt % 2) == 1

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    bx = int(next(it))
    by = int(next(it))
    # Read posts
    posts = [(int(next(it)), int(next(it))) for _ in range(N)]
    # Read rope points (M+1 points: closed polygon)
    poly = [(int(next(it)), int(next(it))) for _ in range(M+1)]
    # Count posts inside polygon
    result = 0
    for px, py in posts:
        if point_in_polygon(px, py, poly):
            result += 1
    # Output minimum posts to remove
    print(result)

if __name__ == '__main__':
    main()
