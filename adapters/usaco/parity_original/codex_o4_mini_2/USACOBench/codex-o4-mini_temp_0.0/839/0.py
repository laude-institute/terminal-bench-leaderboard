#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, W = map(int, data[:2])
    vals = list(map(int, data[2:]))
    w = vals[0::2]
    t = vals[1::2]

    # Check if ratio*1000 >= mid is possible
    def check(mid):
        # dp[j]: max total (t*1000 - mid*w) for weight j (capped at W)
        neg_inf = -10**30
        dp = [neg_inf] * (W + 1)
        dp[0] = 0
        for i in range(N):
            vi = t[i] * 1000 - mid * w[i]
            wi = w[i]
            # iterate backwards to avoid reuse
            for j in range(W, -1, -1):
                if dp[j] != neg_inf:
                    nj = W if j + wi >= W else j + wi
                    v = dp[j] + vi
                    if v > dp[nj]:
                        dp[nj] = v
        return dp[W] >= 0

    # Binary search on integer mid = floor(1000 * ratio)
    low, high = 0, 1000000
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    print(best)

if __name__ == '__main__':
    main()
