#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    positions = [int(next(it)) for _ in range(n)]
    # Read umbrella costs C[1..m]
    C = [0] + [int(next(it)) for _ in range(m)]
    positions.sort()
    INF = 10**18
    # dp[i]: min cost to cover first i cows (1-indexed)
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        # Try covering cows j..i with one umbrella
        for j in range(1, i + 1):
            width = positions[i - 1] - positions[j - 1] + 1
            cost = dp[j - 1] + C[width]
            if cost < dp[i]:
                dp[i] = cost
    # Output result
    print(dp[n])

if __name__ == "__main__":
    main()
