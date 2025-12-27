#!/usr/bin/env python3
"""
Count the number of ways to build the given encrypted string
by applying one or more operations to some source string.
"""
import sys

def count_ways(s, memo):
    # Check memoized result
    if s in memo:
        return memo[s]
    n = len(s)
    # Cannot arise from any operation if too short or even length
    if n < 3 or n % 2 == 0:
        memo[s] = 0
        return 0
    m = (n + 1) // 2
    total = 0
    # Four operation patterns
    # 1) Remove first, attach original at beginning: s = x + x[1:]
    x = s[:m]
    if s[m:] == x[1:]:
        total += 1 + count_ways(x, memo)
    # 2) Remove last, attach original at beginning: s = x + x[:-1]
    if s[m:] == x[:-1]:
        total += 1 + count_ways(x, memo)
    # 3) Remove first, attach original at end: s = x[1:] + x
    x = s[-m:]
    if s[:-m] == x[1:]:
        total += 1 + count_ways(x, memo)
    # 4) Remove last, attach original at end: s = x[:-1] + x
    if s[:-m] == x[:-1]:
        total += 1 + count_ways(x, memo)
    memo[s] = total
    return total

def main():
    s = sys.stdin.readline().strip()
    memo = {}
    print(count_ways(s, memo))

if __name__ == '__main__':
    main()
