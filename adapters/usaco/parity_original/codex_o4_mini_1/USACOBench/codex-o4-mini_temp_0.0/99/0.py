#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    # Read cow positions
    positions = [int(next(it)) for _ in range(N)]
    positions.sort()
    # Read umbrella costs, 1-indexed
    cost = [0] + [int(next(it)) for _ in range(M)]
    # dp[i]: min cost to cover first i cows
    INF = 10**30
    dp = [INF] * (N + 1)
    dp[0] = 0
    # Compute dp
    for i in range(1, N + 1):
        # consider umbrella covering cows j..i
        for j in range(1, i + 1):
            width = positions[i - 1] - positions[j - 1] + 1
            dp[i] = min(dp[i], dp[j - 1] + cost[width])
    # Output result
    print(dp[N])

if __name__ == '__main__':
    main()
