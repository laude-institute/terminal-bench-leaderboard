#!/usr/bin/env python3
"""
Solve the barn painting problem: count area covered exactly K times.
Uses 2D difference array and prefix sums.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    coords = list(map(int, data[2:]))
    # Coordinate range is 0..1000
    MAX = 1001
    # 2D difference array, size (MAX+1)x(MAX+1)
    diff = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    idx = 0
    for _ in range(N):
        x1, y1, x2, y2 = coords[idx:idx+4]
        idx += 4
        diff[x1][y1] += 1
        diff[x2][y1] -= 1
        diff[x1][y2] -= 1
        diff[x2][y2] += 1

    # Build prefix sums to get coat counts
    for x in range(MAX + 1):
        for y in range(MAX + 1):
            if x > 0:
                diff[x][y] += diff[x - 1][y]
            if y > 0:
                diff[x][y] += diff[x][y - 1]
            if x > 0 and y > 0:
                diff[x][y] -= diff[x - 1][y - 1]

    # Count cells with exactly K coats
    area = 0
    for x in range(MAX):
        for y in range(MAX):
            if diff[x][y] == K:
                area += 1

    print(area)

if __name__ == '__main__':
    main()
