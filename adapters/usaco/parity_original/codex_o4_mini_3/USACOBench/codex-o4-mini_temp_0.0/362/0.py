#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    Q = int(next(it))
    # initialize distance matrix
    INF = 10**18
    dist = [[INF]* (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dist[i][i] = 0
    # read flights
    for _ in range(M):
        u = int(next(it)); v = int(next(it)); d = int(next(it))
        if d < dist[u][v]:
            dist[u][v] = d
    # Floyd-Warshall
    for k in range(1, N+1):
        for i in range(1, N+1):
            if dist[i][k] == INF: continue
            dik = dist[i][k]
            row_i = dist[i]
            row_k = dist[k]
            for j in range(1, N+1):
                # compare via k
                new = dik + row_k[j]
                if new < row_i[j]:
                    row_i[j] = new
    # process queries
    valid_count = 0
    total_cost = 0
    # hubs are 1..K
    for _ in range(Q):
        a = int(next(it)); b = int(next(it))
        best = INF
        # must pass through some hub h in [1..K]
        for h in range(1, K+1):
            ca = dist[a][h]
            cb = dist[h][b]
            if ca != INF and cb != INF:
                cost = ca + cb
                if cost < best:
                    best = cost
        if best < INF:
            valid_count += 1
            total_cost += best
    # output
    print(valid_count)
    print(total_cost)

if __name__ == '__main__':
    main()
