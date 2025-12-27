#!/usr/bin/env python3
"""
Read an N x N grid of beauty values and select cow placements so that
every 2x2 sub-grid has exactly 2 cows. Two valid global patterns exist:
 1) Each row alternates cows on even/odd columns (rows independent).
 2) Each column alternates cows on even/odd rows (columns independent).
Compute the maximum beauty for each pattern family and output the larger.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    vals = list(map(int, data[1:]))
    # Build grid as flat list
    # Pattern 1: row-based alternation
    row_sum = 0
    idx = 0
    for i in range(n):
        even_sum = 0
        odd_sum = 0
        for j in range(n):
            v = vals[idx]
            if j & 1:
                odd_sum += v
            else:
                even_sum += v
            idx += 1
        row_sum += max(even_sum, odd_sum)

    # Pattern 2: column-based alternation
    col_sum = 0
    # For each column, sum over even/odd rows
    for j in range(n):
        even_sum = 0
        odd_sum = 0
        # Walk rows
        for i in range(n):
            v = vals[i*n + j]
            if i & 1:
                odd_sum += v
            else:
                even_sum += v
        col_sum += max(even_sum, odd_sum)

    # Output the best of both patterns
    print(max(row_sum, col_sum))

if __name__ == '__main__':
    main()
