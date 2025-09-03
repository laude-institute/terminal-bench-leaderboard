#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    L = int(next(it))
    N = int(next(it))
    rF = int(next(it))
    rB = int(next(it))
    stops = []
    for _ in range(N):
        x = int(next(it))
        c = int(next(it))
        stops.append((x, c))

    # Identify rest stops with maximal tastiness to the end
    best = []  # will hold (x, c) in reverse order
    max_c = 0
    for x, c in reversed(stops):
        if c > max_c:
            best.append((x, c))
            max_c = c
    best.reverse()

    # Compute total tastiness
    total = 0
    cur_x = 0
    dt = rF - rB
    for x, c in best:
        dist = x - cur_x
        # Slack time Bessie can wait
        slack = dist * dt
        total += slack * c
        cur_x = x

    print(total)

if __name__ == '__main__':
    main()
