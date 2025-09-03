#!/usr/bin/env python3
"""
Reads a 3x3 board of uppercase letters and determines:
1. Number of individual cows (single letters) that occupy an entire row, column, or diagonal.
2. Number of distinct two-cow teams (pairs of letters) that occupy entirely a row, column, or diagonal,
   with both cows appearing at least once.
"""

def main():
    # Read the 3x3 board
    board = [input().strip() for _ in range(3)]

    # Collect all lines: 3 rows, 3 columns, 2 diagonals
    lines = []
    # Rows
    for row in board:
        lines.append(list(row))
    # Columns
    for c in range(3):
        lines.append([board[r][c] for r in range(3)])
    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    # Track winning individuals and teams
    winners_single = set()
    winners_team = set()

    for line in lines:
        chars = set(line)
        if len(chars) == 1:
            # Single cow occupies the whole line
            winners_single.add(next(iter(chars)))
        elif len(chars) == 2:
            # Two-cow team occupies the whole line with both cows present
            a, b = sorted(chars)
            winners_team.add((a, b))

    # Output results
    print(len(winners_single))
    print(len(winners_team))

if __name__ == "__main__":
    main()
