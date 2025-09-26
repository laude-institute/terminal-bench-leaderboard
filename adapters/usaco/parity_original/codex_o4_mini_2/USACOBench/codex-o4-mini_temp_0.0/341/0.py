#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    x = int(next(it))
    y = int(next(it))
    z = int(next(it))
    events = []  # list of (temperature, delta)
    # Initial sum: all cows produce x when T < 0
    current = n * x
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        # at T = a, cow moves from cold to comfy: + (y - x)
        events.append((a, y - x))
        # at T = b + 1, cow moves from comfy to hot: + (z - y)
        events.append((b + 1, z - y))
    # Sort events by temperature
    events.sort(key=lambda e: e[0])
    max_milk = current
    # Sweep through events
    i = 0
    m = len(events)
    while i < m:
        t = events[i][0]
        # apply all events at this temperature
        delta_sum = 0
        while i < m and events[i][0] == t:
            delta_sum += events[i][1]
            i += 1
        current += delta_sum
        if current > max_milk:
            max_milk = current
    # Output result
    print(max_milk)

if __name__ == '__main__':
    main()
