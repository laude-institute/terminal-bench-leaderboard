#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N, M = map(int, data[:2])
    A = list(map(int, data[2:2+N]))
    INF = 10**18
    # dp[s] = minimum cost to achieve total area s using processed tiles
    dp = [INF] * (M + 1)
    dp[0] = 0
    # Precompute possible square areas up to M
    max_side = int(M**0.5)
    squares = [i * i for i in range(1, max_side + 1)]
    # Process each tile
    for ai in A:
        newdp = [INF] * (M + 1)
        for s in range(M + 1):
            if dp[s] == INF:
                continue
            # Try exchanging to each possible side length b
            for b, sq in enumerate(squares, start=1):
                ns = s + sq
                if ns > M:
                    break
                cost = dp[s] + (ai - b) * (ai - b)
                if cost < newdp[ns]:
                    newdp[ns] = cost
        dp = newdp
    # Output result
    result = dp[M]
    print(result if result < INF else -1)

if __name__ == '__main__':
    main()
