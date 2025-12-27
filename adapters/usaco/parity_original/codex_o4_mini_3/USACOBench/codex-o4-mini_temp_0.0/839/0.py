#!/usr/bin/env python3
"""
Solution for maximizing talent-to-weight ratio with weight constraint.
Binary search on answer A = floor(1000 * ratio) and check feasibility via DP.
"""
import sys

def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())
    cows = [tuple(map(int, input().split())) for _ in range(N)]  # (w, t)

    # DP weight cap is W; binary search on integer A = floor(1000 * ratio)
    low, high = 0, 1000000  # max possible A is 1000 * max ratio (<=1000)

    def feasible(A):
        # dp[j]: max total modified talent for total weight j (capped at W)
        INF_NEG = -10**18
        dp = [INF_NEG] * (W + 1)
        dp[0] = 0
        for w, t in cows:
            P = 1000 * t - A * w
            # iterate backwards to avoid reuse
            for j in range(W, -1, -1):
                if dp[j] != INF_NEG:
                    j2 = W if j + w >= W else j + w
                    val = dp[j] + P
                    if val > dp[j2]:
                        dp[j2] = val
        return dp[W] >= 0

    # binary search for maximum feasible A
    while low < high:
        mid = (low + high + 1) // 2
        if feasible(mid):
            low = mid
        else:
            high = mid - 1

    print(low)

if __name__ == "__main__":
    main()
