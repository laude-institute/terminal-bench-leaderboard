#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    rects = []
    max_x = max_y = 0
    for _ in range(n):
        x1 = int(next(it)); y1 = int(next(it))
        x2 = int(next(it)); y2 = int(next(it))
        rects.append((x1, y1, x2, y2))
        if x2 > max_x: max_x = x2
        if y2 > max_y: max_y = y2

    # initialize difference array
    size_x = max_x + 1
    size_y = max_y + 1
    diff = [[0] * (size_y + 1) for _ in range(size_x + 1)]

    # apply 2D imos (difference) updates
    for x1, y1, x2, y2 in rects:
        diff[x1][y1] += 1
        diff[x2][y1] -= 1
        diff[x1][y2] -= 1
        diff[x2][y2] += 1

    # prefix sum over x
    for i in range(1, size_x + 1):
        row_prev = diff[i-1]
        row = diff[i]
        for j in range(size_y + 1):
            row[j] += row_prev[j]

    # prefix sum over y
    for i in range(size_x + 1):
        row = diff[i]
        for j in range(1, size_y + 1):
            row[j] += row[j-1]

    # count area with exactly k coats
    area = 0
    for i in range(max_x):
        for j in range(max_y):
            if diff[i][j] == k:
                area += 1

    print(area)

if __name__ == '__main__':
    main()
