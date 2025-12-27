#!/usr/bin/env python3
import sys

def main():
    N = int(sys.stdin.readline())
    segs = []
    for _ in range(N):
        parts = sys.stdin.readline().split()
        t = parts[0]
        a, b = map(int, parts[1:])
        segs.append((t, a, b))

    INF = 10**18
    # Backward pass for initial flow
    low, high = 0, INF
    for t, a, b in reversed(segs):
        if t == 'none':
            low = max(low, a)
            high = min(high, b)
        elif t == 'on':
            low = max(0, low - b)
            high = high - a
        else:  # 'off'
            low = low + a
            high = high + b
    start_low, start_high = low, high

    # Forward pass for final flow
    low, high = 0, INF
    for t, a, b in segs:
        if t == 'none':
            low = max(low, a)
            high = min(high, b)
        elif t == 'on':
            low = low + a
            high = high + b
        else:  # 'off'
            low = max(0, low - b)
            high = high - a
    end_low, end_high = low, high

    print(start_low, start_high)
    print(end_low, end_high)

if __name__ == '__main__':
    main()
