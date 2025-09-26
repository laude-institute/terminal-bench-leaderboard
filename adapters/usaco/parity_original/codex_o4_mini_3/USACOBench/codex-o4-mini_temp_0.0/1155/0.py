#!/usr/bin/env python3
"""
Solution to count lonely photos with exactly one Guernsey or Holstein
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1].strip()
    total = 0
    # For each breed, count substrings with exactly one occurrence and length >= 3
    for breed in ('G', 'H'):
        positions = [-1]
        for i, ch in enumerate(s):
            if ch == breed:
                positions.append(i)
        positions.append(n)
        # For each single occurrence at positions[j]
        for j in range(1, len(positions) - 1):
            L = positions[j] - positions[j - 1]
            R = positions[j + 1] - positions[j]
            # total substrings = L * R
            # subtract those with length < 3: pairs where l_offset + r_offset < 2
            bad = 1
            if L > 1:
                bad += 1
            if R > 1:
                bad += 1
            good = L * R - bad
            if good > 0:
                total += good
    print(total)

if __name__ == '__main__':
    main()
