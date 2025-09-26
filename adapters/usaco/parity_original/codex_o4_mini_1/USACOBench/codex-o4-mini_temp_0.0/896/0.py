#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    mountains = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1])
        idx += 2
        # compute coverage interval on x-axis
        left = x - y
        right = x + y
        mountains.append((left, right))
    # sort by left asc, right desc
    mountains.sort(key=lambda t: (t[0], -t[1]))
    visible = 0
    max_right = -10**20
    # count non-covered intervals
    for l, r in mountains:
        if r > max_right:
            visible += 1
            max_right = r
    print(visible)

if __name__ == '__main__':
    main()
