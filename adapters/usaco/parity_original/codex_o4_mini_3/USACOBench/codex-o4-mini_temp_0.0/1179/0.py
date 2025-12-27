#!/usr/bin/env python3
import sys

def main():
    # Read the answer grid
    answer = [sys.stdin.readline().strip() for _ in range(3)]
    # Read the guess grid
    guess = [sys.stdin.readline().strip() for _ in range(3)]

    # Count green matches and build frequency counts
    green = 0
    ans_count = {}
    guess_count = {}

    for i in range(3):
        for j in range(3):
            a = answer[i][j]
            g = guess[i][j]
            if a == g:
                green += 1
            else:
                ans_count[a] = ans_count.get(a, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1

    # Count yellow matches: min of remaining frequencies
    yellow = 0
    for letter, cnt in guess_count.items():
        yellow += min(cnt, ans_count.get(letter, 0))

    # Output results
    print(green)
    print(yellow)

if __name__ == '__main__':
    main()
