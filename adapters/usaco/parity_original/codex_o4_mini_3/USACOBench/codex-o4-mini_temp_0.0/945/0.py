#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    a = list(map(int, data[2:2+N]))
    # Prefix sums for quick range sum calculation
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + a[i]
    INF = 10**30
    max_segments = K + 1
    # dp[i][s]: min waste for first i groups using s segments
    dp = [[INF] * (max_segments + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    # Base case: one segment covering first i groups
    max_val = 0
    for i in range(1, N+1):
        max_val = max(max_val, a[i-1])
        dp[i][1] = max_val * i - prefix[i]

    # DP transitions for more segments
    for s in range(2, max_segments+1):
        for i in range(1, N+1):
            max_val = 0
            # consider last segment from p to i
            for p in range(i, 0, -1):
                max_val = max(max_val, a[p-1])
                waste = max_val * (i - p + 1) - (prefix[i] - prefix[p-1])
                val = dp[p-1][s-1] + waste
                if val < dp[i][s]:
                    dp[i][s] = val

    # result: exactly K+1 segments
    print(dp[N][max_segments])

if __name__ == "__main__":
    main()
