#!/usr/bin/env python3
import sys

def main():
    # Read input
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Compress consecutive duplicates
    nums = []
    for x in a:
        if not nums or nums[-1] != x:
            nums.append(x)
    m = len(nums)

    # dp[i][j] = min strokes to paint nums[i..j]
    dp = [[0] * m for _ in range(m)]
    for i in range(m):
        dp[i][i] = 1

    # Fill DP for increasing lengths
    for length in range(2, m + 1):
        for i in range(m - length + 1):
            j = i + length - 1
            # Base: paint j separately
            dp[i][j] = dp[i][j - 1] + 1
            # Try merging with same color strokes
            for k in range(i, j):
                if nums[k] == nums[j]:
                    cost = dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0)
                    if cost < dp[i][j]:
                        dp[i][j] = cost

    # Output result for full range
    print(dp[0][m - 1])

if __name__ == '__main__':
    main()
