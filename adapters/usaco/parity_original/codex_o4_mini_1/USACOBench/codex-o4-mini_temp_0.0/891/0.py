#!/usr/bin/env python3
"""
Simulate shell game to maximize correct guesses.
"""

def main():
    import sys

    data = sys.stdin.read().strip().split()
    n = int(data[0])
    # Parse steps: list of (a, b, g)
    steps = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1]); g = int(data[idx+2])
        steps.append((a, b, g))
        idx += 3

    max_score = 0
    # Try each possible starting shell
    for start in (1, 2, 3):
        pos = start
        score = 0
        # Simulate the sequence of swaps and guesses
        for a, b, g in steps:
            # Swap shells a and b
            if pos == a:
                pos = b
            elif pos == b:
                pos = a
            # Check guess
            if g == pos:
                score += 1
        # Track maximum correct guesses
        if score > max_score:
            max_score = score

    # Output the result
    print(max_score)

if __name__ == "__main__":
    main()
