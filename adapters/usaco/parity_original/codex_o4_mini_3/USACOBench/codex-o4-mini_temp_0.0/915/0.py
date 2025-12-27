#!/usr/bin/env python3
import sys

def main():
    # Read and sort positions
    positions = list(map(int, sys.stdin.readline().split()))
    positions.sort()
    a, b, c = positions

    # Compute minimum moves
    if b - a == 1 and c - b == 1:
        min_moves = 0
    elif b - a == 2 or c - b == 2:
        min_moves = 1
    else:
        min_moves = 2

    # Compute maximum moves
    max_moves = max(b - a, c - b) - 1

    # Output results
    print(min_moves)
    print(max_moves)

if __name__ == '__main__':
    main()
