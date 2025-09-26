#!/usr/bin/env python3
import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    # maximum possible side length to consider
    max_side = math.isqrt(M)
    INF = float('inf')
    # dp[s] = minimum cost to reach total area s using processed tiles
    dp = [INF] * (M + 1)
    dp[0] = 0
    for a in A:
        new_dp = [INF] * (M + 1)
        for s in range(M + 1):
            if dp[s] == INF:
                continue
            # try exchanging to every possible new side b
            for b in range(1, max_side + 1):
                area = b * b
                s2 = s + area
                if s2 > M:
                    break
                cost = dp[s] + (a - b) * (a - b)
                if cost < new_dp[s2]:
                    new_dp[s2] = cost
        dp = new_dp
    result = dp[M]
    print(-1 if result == INF else int(result))

if __name__ == '__main__':
    main()
