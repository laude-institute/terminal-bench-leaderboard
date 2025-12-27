#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    W = int(next(it))
    cows = []  # list of (weight, talent)
    for _ in range(n):
        w = int(next(it)); t = int(next(it))
        cows.append((w, t))

    # Check if a given score X is feasible: exists subset with total weight >= W
    # and 1000*total_talent - X*total_weight >= 0
    def feasible(X):
        # dp[j] = max modified sum for total weight j (capped at W)
        INF = 10**18
        dp = [-INF] * (W + 1)
        dp[0] = 0
        for w, t in cows:
            s = 1000 * t - X * w
            # iterate backwards to avoid reuse
            for j in range(W, -1, -1):
                if dp[j] != -INF:
                    nj = W if j + w >= W else j + w
                    val = dp[j] + s
                    if val > dp[nj]:
                        dp[nj] = val
        return dp[W] >= 0

    # Binary search on integer score X
    lo, hi = 0, 1000 * 1000
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1

    # lo is the max floor(1000 * ratio)
    print(lo)

if __name__ == '__main__':
    main()
