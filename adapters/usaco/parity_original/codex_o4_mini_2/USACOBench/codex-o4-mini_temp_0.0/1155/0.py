#!/usr/bin/env python3

import sys

def count_lonely(s, c):
    # Count substrings of length>=3 with exactly one character c
    positions = [0]
    # Record positions (1-based) of character c
    for i, ch in enumerate(s, 1):
        if ch == c:
            positions.append(i)
    # Add sentinel at end
    positions.append(len(s) + 1)
    ans = 0
    # For each occurrence of c, count substrings containing it and no other c
    for i in range(1, len(positions) - 1):
        prev_pos = positions[i - 1]
        curr = positions[i]
        next_pos = positions[i + 1]
        left_choices = curr - prev_pos
        right_choices = next_pos - curr
        # total substrings with this c and no other c
        total = left_choices * right_choices
        # subtract substrings of length < 3: length 1 and length 2
        # length 1: only the cow itself
        total -= 1
        # length 2: extend by one on either side if possible
        if left_choices >= 2:
            total -= 1
        if right_choices >= 2:
            total -= 1
        ans += total
    return ans

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    # N is not used directly
    s = data[1].strip()
    # Count lonely photos for G and H
    result = count_lonely(s, 'G') + count_lonely(s, 'H')
    print(result)

if __name__ == '__main__':
    main()
