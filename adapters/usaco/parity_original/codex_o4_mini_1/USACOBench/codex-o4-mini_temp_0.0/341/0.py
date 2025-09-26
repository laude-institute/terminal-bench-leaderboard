#!/usr/bin/env python3
"""
Solution to Goldilocks and the N Cows problem.
Computes optimal temperature to maximize milk production.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    x = int(next(it))
    y = int(next(it))
    z = int(next(it))
    # Event-based sweep: at temperature t, adjust total milk by delta
    events = {}
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        # At a: cow goes from cold(x) to comfortable(y)
        events[a] = events.get(a, 0) + (y - x)
        # At b+1: cow goes from comfortable(y) to hot(z)
        events[b + 1] = events.get(b + 1, 0) + (z - y)
    # Initial total at very low temperature: all cows cold
    current = n * x
    max_total = current
    # Process events in ascending temperature order
    for t in sorted(events):
        current += events[t]
        if current > max_total:
            max_total = current
    # Output the maximum milk
    print(max_total)

if __name__ == '__main__':
    main()
