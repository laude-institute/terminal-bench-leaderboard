#!/usr/bin/env python3
"""
Solution for merging adjacent equal numbers to maximize the largest value.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    # dp[i][j]: max value if subarray a[i..j] can be merged into one number, else 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    # consider all lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # try splitting point
            for k in range(i, j):
                if dp[i][k] and dp[i][k] == dp[k+1][j]:
                    dp[i][j] = max(dp[i][j], dp[i][k] + 1)
    # find the maximum merged value
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] > ans:
                ans = dp[i][j]
    print(ans)

if __name__ == "__main__":
    main()
