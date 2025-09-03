#!/usr/bin/env python3
"""
Solution to the Wifi Setup problem.
We use dynamic programming on sorted cow positions. dp[j] is the minimum cost to
cover the first j cows. For any segment [i, j], the optimal base station is at
the midpoint, with radius (pos[j] - pos[i]) / 2, costing A + B * radius.
Transitions: dp[j] = min(dp[i-1] + A + B * (pos[j] - pos[i]) / 2) for 1 <= i <= j.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    A = float(next(it))
    B = float(next(it))
    positions = [int(next(it)) for _ in range(n)]
    positions.sort()

    # dp[j]: min cost to cover first j cows
    dp = [float('inf')] * (n + 1)
    dp[0] = 0.0

    for j in range(1, n + 1):
        xj = positions[j-1]
        # try covering cows i..j with one station
        for i in range(1, j + 1):
            xi = positions[i-1]
            radius = (xj - xi) / 2.0
            cost = dp[i-1] + A + B * radius
            if cost < dp[j]:
                dp[j] = cost

    # output result
    # Removing insignificant trailing zeros
    result = dp[n]
    # Print as plain float
    print(result)


if __name__ == '__main__':
    main()
