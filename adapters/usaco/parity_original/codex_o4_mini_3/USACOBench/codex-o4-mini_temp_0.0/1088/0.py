#!/usr/bin/env python3
"""
Solution for placing cows in an N x N grid such that each 2x2 sub-grid
has exactly 2 cows. We choose for each column whether to place cows on
odd rows or even rows to satisfy the condition globally.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    # Read grid values
    # a[i][j] corresponds to row i (0-based), column j (0-based)
    a = [[int(next(it)) for _ in range(n)] for _ in range(n)]

    total_beauty = 0
    # For each column, decide placing cows on odd rows or even rows
    for j in range(n):
        # Sum values in odd-indexed rows (1-based odd -> 0-based even indices)
        sum_odd = 0
        # Sum values in even-indexed rows (1-based even -> 0-based odd indices)
        sum_even = 0
        for i in range(n):
            if i % 2 == 0:
                sum_odd += a[i][j]
            else:
                sum_even += a[i][j]
        total_beauty += max(sum_odd, sum_even)

    # Output the maximum beauty
    print(total_beauty)

if __name__ == '__main__':
    main()
