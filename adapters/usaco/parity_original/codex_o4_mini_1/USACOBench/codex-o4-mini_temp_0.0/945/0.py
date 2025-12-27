#!/usr/bin/env python3
"""
Solution for minimizing net waste by partitioning snake groups.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    a = list(map(int, data[2:2+N]))
    # Prefix sums
    ps = [0] * (N + 1)
    for i in range(N):
        ps[i+1] = ps[i] + a[i]

    # Precompute cost[i][j]: waste for segment a[i..j]
    cost = [[0] * N for _ in range(N)]
    for i in range(N):
        maxv = 0
        for j in range(i, N):
            if a[j] > maxv:
                maxv = a[j]
            cost[i][j] = maxv * (j - i + 1) - (ps[j+1] - ps[i])

    # dp[s][i]: minimum waste for first i+1 groups with s segments
    max_segments = K + 1
    INF = 10**30
    dp = [[INF] * N for _ in range(max_segments + 1)]
    # Base case: one segment
    for i in range(N):
        dp[1][i] = cost[0][i]

    # Fill DP for segments 2..max_segments
    for s in range(2, max_segments + 1):
        for i in range(s-1, N):
            best = INF
            # previous segment end j from s-2 to i-1
            for j in range(s-2, i):
                val = dp[s-1][j] + cost[j+1][i]
                if val < best:
                    best = val
            dp[s][i] = best

    # Result: all N groups with max_segments segments
    print(dp[max_segments][N-1])

if __name__ == '__main__':
    main()
