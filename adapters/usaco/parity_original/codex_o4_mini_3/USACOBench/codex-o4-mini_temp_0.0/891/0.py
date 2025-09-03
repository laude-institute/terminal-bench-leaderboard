#!/usr/bin/env python3
"""
Solution to the shell game problem.

Reads the number of swaps and their details, simulates the pebble's position
for each possible starting shell (1, 2, 3), counts correct guesses, and
outputs the maximum score.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    swaps = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1]); g = int(data[idx+2])
        swaps.append((a, b, g))
        idx += 3

    max_score = 0
    # Try each possible starting position
    for start in (1, 2, 3):
        pos = start
        score = 0
        for a, b, g in swaps:
            # Swap shells if pebble is under one of them
            if pos == a:
                pos = b
            elif pos == b:
                pos = a
            # Check guess
            if pos == g:
                score += 1
        max_score = max(max_score, score)

    print(max_score)

if __name__ == "__main__":
    main()
