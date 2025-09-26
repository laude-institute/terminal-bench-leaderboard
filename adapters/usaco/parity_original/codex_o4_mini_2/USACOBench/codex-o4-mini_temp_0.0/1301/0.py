#!/usr/bin/env python3
"""
Compute the minimum cost for Bessie's Mooloo subscriptions.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    days = list(map(int, data[2:]))
    # dp[i] = min cost to cover days up to days[i-1]
    # dp[i] = days[i-1] + 1 + K + min_{j<=i}(dp[j-1] - days[j-1])
    # Maintain best = min(dp[j-1] - days[j-1])
    best = -days[0]  # dp[0] - days[0]
    dp = 0
    for d in days:
        dp = d + 1 + K + best
        # Update best for next iterations
        best = min(best, dp - d)
    # dp now holds dp[N]
    print(dp)

if __name__ == '__main__':
    main()
