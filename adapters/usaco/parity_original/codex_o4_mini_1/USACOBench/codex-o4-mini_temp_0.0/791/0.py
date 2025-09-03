#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    MOD = 10**9 + 7
    # dp[i]: number of valid paintings of length i
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i <= K:
            # For i <= K, any sequence of colors is possible: M^i
            dp[i] = dp[i-1] * M % MOD
        else:
            # Extend last run or start a new run of length exactly K with a different color
            dp[i] = (dp[i-1] + (M - 1) * dp[i-K]) % MOD
    print(dp[N])

if __name__ == '__main__':
    main()
