#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    V = [int(next(it)) for _ in range(B)]
    R = [int(next(it)) for _ in range(N)]
    # Compute direct contributions C_i
    C = []
    for i in range(N):
        carry = max(R[i-1] - 1, 0) if i > 0 else 0
        c = R[i] - carry
        if c < 0:
            print(-1)
            return
        C.append(c)
    max_c = max(C)
    INF = 10**9
    # Coin change DP to find min coins for each c up to max_c
    dp = [INF] * (max_c + 1)
    dp[0] = 0
    for v in V:
        for amount in range(v, max_c + 1):
            if dp[amount - v] + 1 < dp[amount]:
                dp[amount] = dp[amount - v] + 1
    # Sum up required cows
    total = 0
    for c in C:
        if dp[c] >= INF:
            print(-1)
            return
        total += dp[c]
    print(total)

if __name__ == '__main__':
    main()
