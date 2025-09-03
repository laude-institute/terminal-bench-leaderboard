#!/usr/bin/env python3
"""
Solution to the milking order problem:
Generate all lexicographically sorted permutations of the eight cows,
then select the first ordering that satisfies all adjacency constraints.
"""

import sys
import itertools

def main():
    # List of cows, sorted lexicographically
    cows = [
        "Beatrice", "Belinda", "Bella", "Bessie",
        "Betsy", "Blue", "Buttercup", "Sue"
    ]
    cows.sort()

    # Read constraints
    n = int(sys.stdin.readline().strip())
    constraints = []  # list of (cow1, cow2) pairs
    for _ in range(n):
        parts = sys.stdin.readline().split()
        a = parts[0]
        b = parts[-1]
        constraints.append((a, b))

    # Try each permutation in lexicographic order
    for perm in itertools.permutations(cows):
        valid = True
        for a, b in constraints:
            # Check adjacency
            if abs(perm.index(a) - perm.index(b)) != 1:
                valid = False
                break
        if valid:
            # Print the first valid ordering
            for cow in perm:
                print(cow)
            return

if __name__ == "__main__":
    main()
