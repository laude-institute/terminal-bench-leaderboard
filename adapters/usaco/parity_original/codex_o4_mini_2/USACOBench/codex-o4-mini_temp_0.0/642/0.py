#!/usr/bin/env python3
import sys
import itertools

def main():
    input = sys.stdin.readline
    n = int(input())
    pts = []
    for i in range(n):
        x, y = map(int, input().split())
        pts.append((x, y, i))

    # sort by x and y
    sx = sorted((x, idx) for x, y, idx in pts)
    sy = sorted((y, idx) for x, y, idx in pts)

    # gather candidate indices from extremes
    cand = set()
    for i in range(4):
        cand.add(sx[i][1])
        cand.add(sx[-1-i][1])
        cand.add(sy[i][1])
        cand.add(sy[-1-i][1])
    cand_list = list(cand)

    # function to compute area after removing some indices
    def area_after(rem):
        rem = set(rem)
        # min x
        for x, idx in sx:
            if idx not in rem:
                xmin = x
                break
        # max x
        for x, idx in reversed(sx):
            if idx not in rem:
                xmax = x
                break
        # min y
        for y, idx in sy:
            if idx not in rem:
                ymin = y
                break
        # max y
        for y, idx in reversed(sy):
            if idx not in rem:
                ymax = y
                break
        return (xmax - xmin) * (ymax - ymin)

    ans = float('inf')
    # try removing up to 3 cows
    for k in range(4):
        for rem in itertools.combinations(cand_list, k):
            a = area_after(rem)
            if a < ans:
                ans = a
    print(ans)

if __name__ == '__main__':
    main()
