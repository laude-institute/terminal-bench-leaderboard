#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    x, y = map(int, data)
    curr = x
    total_dist = 0
    # Zig-zag search: distances 1,2,4,... with alternating direction
    k = 0
    while True:
        step = 1 << k
        # Determine next target position
        if k % 2 == 0:
            nxt = x + step
        else:
            nxt = x - step
        # If Bessie is between curr and nxt, finish at y
        if min(curr, nxt) <= y <= max(curr, nxt):
            total_dist += abs(y - curr)
            break
        # Otherwise, travel full segment and continue
        total_dist += abs(nxt - curr)
        curr = nxt
        k += 1
    print(total_dist)

if __name__ == '__main__':
    main()
