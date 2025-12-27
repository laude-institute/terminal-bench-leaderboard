#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    INF = 10**18
    # Read inputs
    N, M, K, Q = map(int, input().split())
    # Initialize distance matrix
    d = [[INF] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    # Read edges
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if w < d[u][v]:
            d[u][v] = w
    # Floyd-Warshall up to hub index K
    for k in range(K):
        for i in range(N):
            dik = d[i][k]
            if dik == INF:
                continue
            row_k = d[k]
            row_i = d[i]
            for j in range(N):
                val = dik + row_k[j]
                if val < row_i[j]:
                    row_i[j] = val
    # Process queries
    count = 0
    total = 0
    for _ in range(Q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        best = INF
        # Ensure path goes through at least one hub
        for h in range(K):
            if d[a][h] != INF and d[h][b] != INF:
                cost = d[a][h] + d[h][b]
                if cost < best:
                    best = cost
        if best < INF:
            count += 1
            total += best
    # Output results
    print(count)
    print(total)

if __name__ == "__main__":
    main()
