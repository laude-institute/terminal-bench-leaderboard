#!/usr/bin/env python3
"""
Maximize the number of "MOO" words in a ciphered grid under a substitution cipher.
"""

import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, m = map(int, data[:2])
    grid = data[2:2 + n]
    # All eight directions (dx, dy)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    max_count = 0
    # Try every possible mapping of encrypted char -> 'M' and -> 'O'
    for eM in map(chr, range(ord('A'), ord('Z') + 1)):
        # no letter maps to itself
        if eM == 'M':
            continue
        for eO in map(chr, range(ord('A'), ord('Z') + 1)):
            if eO == eM or eO == 'O':
                continue
            count = 0
            # Count occurrences of pattern [eM, eO, eO]
            for i in range(n):
                for j in range(m):
                    if grid[i][j] != eM:
                        continue
                    for dx, dy in directions:
                        i1, j1 = i + dx, j + dy
                        i2, j2 = i + 2*dx, j + 2*dy
                        if 0 <= i1 < n and 0 <= j1 < m and 0 <= i2 < n and 0 <= j2 < m:
                            if grid[i1][j1] == eO and grid[i2][j2] == eO:
                                count += 1
            if count > max_count:
                max_count = count
    print(max_count)

if __name__ == '__main__':
    main()
