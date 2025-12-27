#!/usr/bin/env python3
"""
Reads a 3x3 answer grid and a 3x3 guess grid from stdin,
computes number of green (correct position) and yellow (correct letter, wrong position) hints,
and prints the results.
"""
import sys

def main():
    # Read the answer and guess grids
    answer = [sys.stdin.readline().strip() for _ in range(3)]
    guess = [sys.stdin.readline().strip() for _ in range(3)]

    green = 0
    # Counts for letters that are not green
    ans_count = {}
    guess_count = {}

    # First pass: count greens and accumulate non-green letters
    for i in range(3):
        for j in range(3):
            a = answer[i][j]
            g = guess[i][j]
            if g == a:
                green += 1
            else:
                ans_count[a] = ans_count.get(a, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1

    # Second pass: count yellows based on min overlap of counts
    yellow = 0
    for letter, count in guess_count.items():
        yellow += min(count, ans_count.get(letter, 0))

    # Output the results
    print(green)
    print(yellow)

if __name__ == '__main__':
    main()
