#!/usr/bin/env python3
import sys
import itertools

def main():
    # List cows in alphabetical order
    cows = sorted([
        "Bessie", "Buttercup", "Belinda", "Beatrice",
        "Bella", "Blue", "Betsy", "Sue"
    ])
    # Read number of constraints
    N = int(sys.stdin.readline().strip())
    constraints = []
    # Parse constraints
    for _ in range(N):
        parts = sys.stdin.readline().strip().split()
        x = parts[0]
        y = parts[-1]
        constraints.append((x, y))

    # Try all permutations in lex order
    for perm in itertools.permutations(cows):
        pos = {cow: i for i, cow in enumerate(perm)}
        valid = True
        # Check adjacency constraints
        for x, y in constraints:
            if abs(pos[x] - pos[y]) != 1:
                valid = False
                break
        if valid:
            # Output valid order
            for cow in perm:
                print(cow)
            return

if __name__ == "__main__":
    main()
