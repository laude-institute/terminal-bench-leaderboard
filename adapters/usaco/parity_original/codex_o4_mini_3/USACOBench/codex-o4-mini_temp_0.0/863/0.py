#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n, k = map(int, data[:2])
    skills = list(map(int, data[2:2+n]))
    # dp[i]: max sum for first i cows
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_skill = 0
        # try all team sizes ending at i
        for j in range(1, min(k, i) + 1):
            max_skill = max(max_skill, skills[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_skill * j)
    # output result for all n cows
    print(dp[n])

if __name__ == "__main__":
    main()
