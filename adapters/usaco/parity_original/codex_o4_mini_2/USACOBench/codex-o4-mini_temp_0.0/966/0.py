#!/usr/bin/env python3
"""
Given N, find the N-th positive integer that is not divisible by 3 or 5.
"""
import sys

def count_good(x):
    # Count numbers <= x not divisible by 3 or 5 via inclusion-exclusion
    return x - x // 3 - x // 5 + x // 15

def find_nth(n):
    # Binary search for smallest x with count_good(x) >= n
    lo, hi = 1, n * 5
    while lo < hi:
        mid = (lo + hi) // 2
        if count_good(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)
    result = find_nth(n)
    print(result)

if __name__ == '__main__':
    main()
