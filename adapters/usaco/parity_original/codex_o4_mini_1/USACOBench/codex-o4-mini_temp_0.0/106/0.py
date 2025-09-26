#!/usr/bin/env python3
"""
Compute the minimum time for FJ to visit all farms in order and return to start,
avoiding stepping on any farm (except start/end). Axis-aligned segments
with intermediate farms require a detour of +2.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    farms = [(0, 0)] * n
    for i in range(n):
        x = int(next(it)); y = int(next(it))
        farms[i] = (x, y)
    total = 0
    # iterate through farm 1->2->...->N->1
    for i in range(n):
        x1, y1 = farms[i]
        x2, y2 = farms[(i+1) % n]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        dist = dx + dy
        # check for blocking farm on straight segment
        if x1 == x2:
            # vertical move
            ymin, ymax = sorted((y1, y2))
            for j in range(n):
                if j == i or j == (i+1) % n:
                    continue
                xj, yj = farms[j]
                if xj == x1 and ymin < yj < ymax:
                    dist += 2
                    break
        elif y1 == y2:
            # horizontal move
            xmin, xmax = sorted((x1, x2))
            for j in range(n):
                if j == i or j == (i+1) % n:
                    continue
                xj, yj = farms[j]
                if yj == y1 and xmin < xj < xmax:
                    dist += 2
                    break
        total += dist
    # output result
    print(total)

if __name__ == '__main__':
    main()
