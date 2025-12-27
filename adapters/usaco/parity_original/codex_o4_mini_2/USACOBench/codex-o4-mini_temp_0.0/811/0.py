#!/usr/bin/env python3
"""
Snow Boots Problem
"""
import sys

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    f = list(map(int, input().split()))
    boots = [tuple(map(int, input().split())) for _ in range(B)]
    # dp[j][i]: minimum discards to reach tile i with boot j (0-based indices)
    INF = 10**18
    dp = [[INF] * N for _ in range(B)]
    # Initial: put on boot j as first boot, discarding j boots above it
    for j in range(B):
        s_j, d_j = boots[j]
        if s_j >= f[0]:
            dp[j][0] = j

    # Process boots in increasing order
    for j in range(B):
        s_j, d_j = boots[j]
        # Boot change transitions: from earlier boots p to current boot j
        for p in range(j):
            if boots[p][0] < 0:
                continue
            for i in range(N):
                if dp[p][i] < INF and s_j >= f[i]:
                    cost = dp[p][i] + (j - p)
                    if cost < dp[j][i]:
                        dp[j][i] = cost
        # Movement transitions: step forward with current boot j
        for i in range(N):
            if dp[j][i] < INF:
                # can step up to d_j forward
                max_step = d_j
                for k in range(i+1, min(N, i + max_step + 1)):
                    if f[k] <= s_j and dp[j][i] < dp[j][k]:
                        dp[j][k] = dp[j][i]

    # Answer: min discards among boots at tile N-1
    result = min(dp[j][N-1] for j in range(B))
    print(result)


if __name__ == '__main__':
    main()
