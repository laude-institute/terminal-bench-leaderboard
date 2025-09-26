#!/usr/bin/env python3
"""
Count maximal matchings between cows and barns under size constraints.
"""
import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s.sort()
    t.sort()
    # f[i]: first barn index (1-based) that cow i can fit; N+1 if none
    f = [0] * N
    pos = 0
    for i in range(N):
        while pos < N and t[pos] < s[i]:
            pos += 1
        f[i] = pos + 1  # 1-based
    # dp[i][j]: ways to assign first i cows into first j barns
    # we only keep previous row
    dp_prev = [1] * (N + 1)
    ways = [0] * (N + 1)
    ways[0] = 1
    for i in range(1, N + 1):
        dp_curr = [0] * (N + 1)
        # cow index i-1, threshold f[i-1]
        th = f[i-1]
        for j in range(1, N + 1):
            # skip barn j
            dp_curr[j] = dp_curr[j-1]
            # use barn j if fits
            if j >= th:
                dp_curr[j] = (dp_curr[j] + dp_prev[j-1]) % MOD
        ways[i] = dp_curr[N]
        dp_prev = dp_curr
    # L[i]: number of barns cow i can fit
    L = [0] * (N + 1)
    for i in range(1, N + 1):
        if f[i-1] <= N:
            L[i] = N - f[i-1] + 1
        else:
            L[i] = 0
    # sum over valid k
    result = 0
    for k in range(0, N):
        # k matched cows, check cow k+1 unmatched: L[k+1] <= k
        if L[k+1] <= k:
            result = (result + ways[k]) % MOD
    # k = N always valid
    result = (result + ways[N]) % MOD
    print(result)

if __name__ == '__main__':
    main()
