#!/usr/bin/env python3
"""
Reads adjacency constraints among eight cows and finds the lexicographically
smallest ordering satisfying all constraints.
"""
import sys
import itertools

def main():
    # List of all cows
    cows = [
        "Bessie", "Buttercup", "Belinda", "Beatrice",
        "Bella", "Blue", "Betsy", "Sue"
    ]
    cows.sort()
    # Read number of constraints
    n = int(sys.stdin.readline().strip())
    constraints = []  # list of (cow1, cow2) pairs
    for _ in range(n):
        parts = sys.stdin.readline().split()
        # Format: X must be milked beside Y
        x = parts[0]
        y = parts[-1]
        constraints.append((x, y))

    # Try each permutation in lex order
    for perm in itertools.permutations(cows):
        pos = {cow: i for i, cow in enumerate(perm)}
        valid = True
        for x, y in constraints:
            if abs(pos[x] - pos[y]) != 1:
                valid = False
                break
        if valid:
            # Found the first valid ordering
            for cow in perm:
                print(cow)
            return

if __name__ == "__main__":
    main()
