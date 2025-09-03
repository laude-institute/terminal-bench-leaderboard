#!/usr/bin/env python3
"""
Dynamic programming solution for grouping cows into teams.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    skills = list(map(int, data[2:]))
    # dp[i] = max sum of skill levels for first i cows
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        max_skill = 0
        # consider team ending at cow i of size j
        for j in range(1, min(K, i) + 1):
            # update max skill in this team
            if skills[i - j] > max_skill:
                max_skill = skills[i - j]
            # update dp
            current = dp[i - j] + max_skill * j
            if current > dp[i]:
                dp[i] = current
    # output the result for all N cows
    print(dp[N])

if __name__ == '__main__':
    main()
