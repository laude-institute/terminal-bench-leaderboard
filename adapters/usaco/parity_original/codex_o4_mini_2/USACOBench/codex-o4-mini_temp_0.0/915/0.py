#!/usr/bin/env python3
"""
Solution to the cow herding problem.
Reads three integer positions, computes the minimum and maximum moves
to arrange cows in three consecutive positions under given rules.
"""
import sys

def main():
    # Read and sort positions
    positions = list(map(int, sys.stdin.read().strip().split()))
    positions.sort()
    a, b, c = positions

    # Compute minimum moves
    # If already consecutive, no moves needed
    if b - a == 1 and c - b == 1:
        min_moves = 0
    # If there's exactly one gap of size 2, one move can fill it
    elif b - a == 2 or c - b == 2:
        min_moves = 1
    # Otherwise, it always takes two moves
    else:
        min_moves = 2

    # Compute maximum moves as the larger gap minus one
    max_moves = max(b - a, c - b) - 1

    # Output results
    print(min_moves)
    print(max_moves)

if __name__ == "__main__":
    main()
