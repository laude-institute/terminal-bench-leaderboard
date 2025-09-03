#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    segments = []
    for _ in range(N):
        parts = input().split()
        typ = parts[0]
        a, b = map(int, parts[1:])
        segments.append((typ, a, b))
    # Use a large number as infinity
    INF = 10**18
    # Reverse pass to compute initial flow range
    low, high = 0, INF
    for typ, a, b in reversed(segments):
        if typ == 'none':
            # Flow must be within sensor range
            low = max(low, a)
            high = min(high, b)
        elif typ == 'on':
            # In reverse, subtract the on-ramp contribution
            low = max(0, low - b)
            high = high - a
        elif typ == 'off':
            # In reverse, add back the off-ramp exit
            low = low + a
            high = high + b
    initial_low, initial_high = low, high

    # Forward pass to compute final flow range
    low, high = initial_low, initial_high
    for typ, a, b in segments:
        if typ == 'none':
            low = max(low, a)
            high = min(high, b)
        elif typ == 'on':
            low = low + a
            high = high + b
        elif typ == 'off':
            low = max(0, low - b)
            high = high - a
    final_low, final_high = low, high

    # Output the results
    print(initial_low, initial_high)
    print(final_low, final_high)


if __name__ == '__main__':
    main()
