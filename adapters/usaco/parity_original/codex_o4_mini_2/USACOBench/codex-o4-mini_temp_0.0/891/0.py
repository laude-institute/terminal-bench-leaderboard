#!/usr/bin/env python3
"""
Simulate the shell game to determine the maximum correct guesses
for unknown initial pebble location.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    # Parse steps: triples of (a, b, g)
    steps = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1]); g = int(data[idx+2])
        steps.append((a, b, g))
        idx += 3

    best = 0
    # Try each possible starting position
    for start in (1, 2, 3):
        pos = start
        score = 0
        for a, b, g in steps:
            # Swap shells
            if pos == a:
                pos = b
            elif pos == b:
                pos = a
            # Count guess
            if g == pos:
                score += 1
        best = max(best, score)

    print(best)

if __name__ == '__main__':
    main()
