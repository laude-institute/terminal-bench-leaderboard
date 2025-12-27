#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(next(it))

    # Precompute cost[l][r]: mismatches if breakout at day l, next at r+1
    # Segment days l..r have expected values 0,1,2,...
    cost = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(1, n + 1):
        mism = 0
        for r in range(l, n + 1):
            expected = r - l
            if a[r] != expected:
                mism += 1
            cost[l][r] = mism

    # dp[r][j]: min mismatches for days 1..r with j breakouts (segments)
    INF = 10**9
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    # Build DP
    for r in range(1, n + 1):
        for j in range(1, r + 1):
            # last segment from t+1 to r, where t >= j-1
            best = INF
            # optimize by scanning t
            for t in range(j-1, r):
                prev = dp[t][j-1]
                if prev >= INF:
                    continue
                c = cost[t+1][r]
                v = prev + c
                if v < best:
                    best = v
            dp[r][j] = best

    # Output results for k = 1..n
    out = []
    for k in range(1, n + 1):
        res = dp[n][k]
        out.append(str(res))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
