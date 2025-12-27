#!/usr/bin/env python3
"""
Reads input specifying trail length, number of rest stops, and walking rates.
Selects optimal rest stops to maximize tastiness without falling behind Farmer John.
"""
import sys

def main():
    data = sys.stdin.read().split()
    L, N, rF, rB = map(int, data[:4])
    stops = []  # list of (position, tastiness)
    idx = 4
    for _ in range(N):
        x = int(data[idx]); c = int(data[idx+1])
        stops.append((x, c))
        idx += 2

    # Identify rest stops with highest tastiness from right to left
    best_stops = []
    max_c = 0
    for x, c in reversed(stops):
        if c > max_c:
            best_stops.append((x, c))
            max_c = c
    best_stops.reverse()

    # Accumulate total tastiness
    prev_x = 0
    total = 0
    delta_rate = rF - rB
    for x, c in best_stops:
        dist = x - prev_x
        total += dist * delta_rate * c
        prev_x = x

    # Output result
    print(total)

if __name__ == '__main__':
    main()
