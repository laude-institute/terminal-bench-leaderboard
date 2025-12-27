#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    skills = [int(next(it)) for _ in range(n)]

    # dp[i] = max total skill for first i cows
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_skill = 0
        # consider teams ending at i of size j
        for j in range(1, min(k, i) + 1):
            max_skill = max(max_skill, skills[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_skill * j)

    print(dp[n])

if __name__ == '__main__':
    main()
