# 1. Restate the problem in plain English
# We have a 3x3 tic-tac-toe board filled with letters A-Z. We need to find:
#  - How many single cows (letters) occupy an entire row, column, or diagonal.
#  - How many distinct pairs of cows (two letters) jointly occupy an entire row, column, or diagonal,
#    with both letters appearing at least once in that line.
#
# 2. Conceptual solution in plain English
#  - Read the 3x3 board as a list of strings.
#  - Define all 8 winning lines (3 rows, 3 columns, 2 diagonals).
#  - For each line:
#      * If all three characters are the same, record that letter as a single winner.
#      * If the line contains exactly two distinct letters, record that unordered pair as a team winner.
#  - Count unique single winners and unique team winners.
#
# 3. Pseudocode
#  read board lines
#  build list of lines (rows, columns, diagonals)
#  initialize empty set single_winners
#  initialize empty set team_winners
#  for each line in lines:
#      letters = set(line)
#      if len(letters) == 1:
#          add the single letter to single_winners
#      elif len(letters) == 2:
#          sort the two letters as a tuple and add to team_winners
#  print size of single_winners
#  print size of team_winners

import sys

def main():
    # Read the 3x3 board
    board = [sys.stdin.readline().strip() for _ in range(3)]

    # Collect all winning lines
    lines = []
    # Rows
    lines.extend([list(row) for row in board])
    # Columns
    for c in range(3):
        lines.append([board[r][c] for r in range(3)])
    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    single_winners = set()
    team_winners = set()

    for line in lines:
        uniq = set(line)
        if len(uniq) == 1:
            # Single cow wins
            single_winners.add(next(iter(uniq)))
        elif len(uniq) == 2:
            # Two-cow team wins, ensure both appear
            team = tuple(sorted(uniq))
            team_winners.add(team)

    # Output results
    print(len(single_winners))
    print(len(team_winners))

if __name__ == "__main__":
    main()
