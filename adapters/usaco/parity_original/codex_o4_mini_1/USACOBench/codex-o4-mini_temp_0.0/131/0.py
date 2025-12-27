#!/usr/bin/env python3
"""
Solution to the 'Three Lines' problem.
Determines if all points can be covered by at most three axis-aligned lines.
"""

import sys

sys.setrecursionlimit(1000000)

def can_cover(points, k):
    """
    Recursively checks if all points can be covered by k horizontal or vertical lines.
    Picks the first point and tries covering its x or y line.
    """
    if not points:
        return True
    if k == 0:
        return False
    # Take an arbitrary point
    x0, y0 = points[0]
    # Try vertical line x = x0
    rem_x = [p for p in points if p[0] != x0]
    if can_cover(rem_x, k - 1):
        return True
    # Try horizontal line y = y0
    rem_y = [p for p in points if p[1] != y0]
    if can_cover(rem_y, k - 1):
        return True
    return False

def main():
    input = sys.stdin.readline
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    # Check if coverable with three lines
    result = 1 if can_cover(points, 3) else 0
    print(result)

if __name__ == "__main__":
    main()
