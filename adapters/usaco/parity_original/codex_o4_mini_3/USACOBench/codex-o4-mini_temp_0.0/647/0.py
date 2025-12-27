#!/usr/bin/env python3
"""
Bessie merging game: maximize largest number via adjacent merging.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    # dp[i][j]: value when interval [i..j] fully merges, or 0 if not mergeable
    dp = [[0] * n for _ in range(n)]
    ans = 0
    # base cases: single elements
    for i in range(n):
        dp[i][i] = arr[i]
        ans = max(ans, arr[i])
    # consider all lengths from 2 to n
    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i + length - 1
            # try splitting at k
            for k in range(i, j):
                if dp[i][k] and dp[i][k] == dp[k+1][j]:
                    dp[i][j] = max(dp[i][j], dp[i][k] + 1)
            ans = max(ans, dp[i][j])
    print(ans)

if __name__ == '__main__':
    main()
