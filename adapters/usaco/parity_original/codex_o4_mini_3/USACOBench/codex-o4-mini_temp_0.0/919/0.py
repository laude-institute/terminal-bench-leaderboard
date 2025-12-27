#!/usr/bin/env python3
"""
Compute the area covered by exactly K overlapping rectangles.
Uses 2D prefix sum (difference array) on integer grid.
"""
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    rects = []
    max_x = max_y = 0
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2))
        if x2 > max_x: max_x = x2
        if y2 > max_y: max_y = y2

    # Initialize 2D difference array
    # We need indices 0..max_x and 0..max_y inclusive
    diff = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    # Apply rectangle updates
    for x1, y1, x2, y2 in rects:
        diff[x1][y1] += 1
        diff[x2][y1] -= 1
        diff[x1][y2] -= 1
        diff[x2][y2] += 1

    # Build prefix sums
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            if i > 0:
                diff[i][j] += diff[i - 1][j]
            if j > 0:
                diff[i][j] += diff[i][j - 1]
            if i > 0 and j > 0:
                diff[i][j] -= diff[i - 1][j - 1]

    # Count area where coverage == K
    area = 0
    # Each cell (i,j) represents unit square [i,i+1) x [j,j+1)
    for i in range(max_x):
        for j in range(max_y):
            if diff[i][j] == K:
                area += 1

    print(area)

if __name__ == '__main__':
    main()
