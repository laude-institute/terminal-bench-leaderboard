#!/usr/bin/env python3
import sys

def main():
    # Read the answer and guess grids
    answer = [sys.stdin.readline().strip() for _ in range(3)]
    guess = [sys.stdin.readline().strip() for _ in range(3)]

    green = 0
    # Lists to hold unmatched letters for yellow counting
    answer_unmatched = []
    guess_unmatched = []

    # Compute greens and collect unmatched letters
    for i in range(3):
        for j in range(3):
            if answer[i][j] == guess[i][j]:
                green += 1
            else:
                answer_unmatched.append(answer[i][j])
                guess_unmatched.append(guess[i][j])

    # Count occurrences of each breed in unmatched lists
    count_ans = {}
    for ch in answer_unmatched:
        count_ans[ch] = count_ans.get(ch, 0) + 1
    count_guess = {}
    for ch in guess_unmatched:
        count_guess[ch] = count_guess.get(ch, 0) + 1

    # Compute yellows: sum of minimum matches per letter
    yellow = 0
    for ch, cnt in count_guess.items():
        yellow += min(cnt, count_ans.get(ch, 0))

    # Output results
    print(green)
    print(yellow)

if __name__ == "__main__":
    main()
