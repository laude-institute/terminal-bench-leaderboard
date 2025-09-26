#!/usr/bin/env python3
"""
Reads an array of colors and computes the minimum number of brush strokes
needed to paint the array by painting contiguous intervals of a single color.
Uses interval dynamic programming (O(N^3) time, N <= 300).
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    a = list(map(int, input().split()))
    # dp[i][j]: minimum strokes to paint subarray a[i..j]
    dp = [[0] * N for _ in range(N)]
    # Build up from shorter to longer intervals
    for i in range(N - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, N):
            # Base: paint a[j] separately after [i..j-1]
            dp[i][j] = dp[i][j - 1] + 1
            # Try merging with a matching color before j
            for k in range(i, j):
                if a[k] == a[j]:
                    # if k+1 > j-1, that part takes 0 strokes
                    mid = dp[k + 1][j - 1] if k + 1 <= j - 1 else 0
                    dp[i][j] = min(dp[i][j], dp[i][k] + mid)
    print(dp[0][N - 1])

if __name__ == '__main__':
    main()
