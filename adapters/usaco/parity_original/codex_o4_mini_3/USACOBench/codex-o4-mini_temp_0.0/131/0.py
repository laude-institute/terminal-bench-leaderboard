#!/usr/bin/env python3
import sys

def can_cover(pts, k):
    # Base cases
    if not pts:
        return True
    if k == 0:
        return False
    # Choose first point to define a line
    x0, y0 = pts[0]
    # Try placing vertical line x = x0
    rem = [p for p in pts if p[0] != x0]
    if can_cover(rem, k - 1):
        return True
    # Try placing horizontal line y = y0
    rem = [p for p in pts if p[1] != y0]
    if can_cover(rem, k - 1):
        return True
    return False

def main():
    input = sys.stdin.readline
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    # Use 3 lines
    possible = can_cover(pts, 3)
    print(1 if possible else 0)

if __name__ == "__main__":
    main()
