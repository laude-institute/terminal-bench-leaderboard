#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    # dp[s] = min cost to reach total area s using processed tiles
    INF = 10**18
    dp = [INF] * (M + 1)
    dp[0] = 0
    max_b = int(M**0.5)
    for a in A:
        ndp = [INF] * (M + 1)
        for s in range(M + 1):
            if dp[s] == INF:
                continue
            # try all possible new side lengths b
            for b in range(1, max_b + 1):
                ns = s + b * b
                if ns > M:
                    continue
                cost = dp[s] + (a - b) * (a - b)
                if cost < ndp[ns]:
                    ndp[ns] = cost
        dp = ndp
    res = dp[M]
    print(res if res < INF else -1)

if __name__ == "__main__":
    main()
