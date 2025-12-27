#!/usr/bin/env python3
"""
Reads a 3x3 tic-tac-toe board with cow initials and counts:
1) Number of individual cows who claim victory.
2) Number of two-cow teams who claim victory.
"""
import sys

def main():
    # Read the 3x3 board
    grid = [sys.stdin.readline().strip() for _ in range(3)]
    # Collect all rows, columns, and diagonals
    lines = []
    # Rows
    for row in grid:
        lines.append(list(row))
    # Columns
    for c in range(3):
        lines.append([grid[r][c] for r in range(3)])
    # Diagonals
    lines.append([grid[i][i] for i in range(3)])
    lines.append([grid[i][2 - i] for i in range(3)])

    singles = set()
    teams = set()

    for line in lines:
        unique = set(line)
        if len(unique) == 1:
            # Single cow wins
            singles.add(next(iter(unique)))
        elif len(unique) == 2:
            # Two-cow team wins if both appear
            a, b = sorted(unique)
            teams.add((a, b))

    # Output results
    print(len(singles))
    print(len(teams))

if __name__ == "__main__":
    main()
