#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    mountains = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        # compute left and right endpoints of the mountain base
        left = x - y
        right = x + y
        mountains.append((left, right))
    # sort by left ascending, right descending
    mountains.sort(key=lambda lr: (lr[0], -lr[1]))
    visible = 0
    max_right = -10**30
    for left, right in mountains:
        # if current mountain extends beyond all previous, it's visible
        if right > max_right:
            visible += 1
            max_right = right
    print(visible)

if __name__ == '__main__':
    main()
