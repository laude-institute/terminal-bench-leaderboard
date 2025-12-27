#!/usr/bin/env python3
"""
Farm Painting: count enclosures not contained by others.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    rects = []
    ys = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2))
        ys.append(y1)

    # Coordinate compress y1 values
    ys_unique = sorted(set(ys))
    y1_to_i = {y: i + 1 for i, y in enumerate(ys_unique)}
    M = len(ys_unique)

    # Sort by x1 asc, x2 desc to ensure potential containers seen first
    rects.sort(key=lambda r: (r[0], -r[2]))

    # Fenwick tree for prefix max queries on y2
    tree = [0] * (M + 1)

    def update(i, value):
        # point update: set max
        while i <= M:
            if tree[i] < value:
                tree[i] = value
            i += i & -i

    def query(i):
        # prefix max query up to i
        res = 0
        while i > 0:
            if tree[i] > res:
                res = tree[i]
            i -= i & -i
        return res

    count = 0
    for x1, y1, x2, y2 in rects:
        idx = y1_to_i[y1]
        # check if contained by any active rectangle
        if query(idx) >= y2:
            continue
        # not contained: add as potential container
        count += 1
        update(idx, y2)

    print(count)


if __name__ == '__main__':
    main()
