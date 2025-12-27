#!/usr/bin/env python3
"""
Goldilocks and the N Cows
Compute optimal thermostat setting to maximize milk production.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    x = int(next(it))
    y = int(next(it))
    z = int(next(it))
    events = {}
    # Initial baseline: all cows produce x when T < any Ai
    curr = x * n
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        # At T = a, cow goes cold->comfortable
        events[a] = events.get(a, 0) + (y - x)
        # At T = b+1, cow goes comfortable->hot
        events[b + 1] = events.get(b + 1, 0) + (z - y)
    # Sweep through events in order
    best = curr
    for t in sorted(events):
        curr += events[t]
        if curr > best:
            best = curr
    print(best)

if __name__ == '__main__':
    main()
