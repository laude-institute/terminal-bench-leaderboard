#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for i in range(N):
        x, y = map(int, input().split())
        cows.append((x, y, i))

    # Sort by x and y
    xs = sorted((x, i) for x, y, i in cows)
    ys = sorted((y, i) for x, y, i in cows)

    # Collect candidate cows to remove
    candidates = set()
    for arr in (xs, ys):
        for val, idx in arr[:2] + arr[-2:]:
            candidates.add(idx)

    # For quick coord lookup by index
    xi = [0]*N
    yi = [0]*N
    for x, y, idx in cows:
        xi[idx] = x
        yi[idx] = y

    best = float('inf')
    # Evaluate removal of candidate cows
    for idx in candidates:
        # Determine new boundaries
        if xs[0][1] != idx:
            min_x = xs[0][0]
        else:
            min_x = xs[1][0]
        if xs[-1][1] != idx:
            max_x = xs[-1][0]
        else:
            max_x = xs[-2][0]
        if ys[0][1] != idx:
            min_y = ys[0][0]
        else:
            min_y = ys[1][0]
        if ys[-1][1] != idx:
            max_y = ys[-1][0]
        else:
            max_y = ys[-2][0]

        area = (max_x - min_x) * (max_y - min_y)
        if area < best:
            best = area

    # If no candidates, area is 0
    if best == float('inf'):
        best = 0

    print(best)

if __name__ == '__main__':
    main()
