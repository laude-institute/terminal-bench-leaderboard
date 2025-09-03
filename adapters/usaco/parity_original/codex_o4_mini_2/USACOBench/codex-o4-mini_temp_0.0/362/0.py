#!/usr/bin/env python3
"""
Problem Restatement:
Given a directed, weighted graph with N farms (nodes) and M one-way flights (edges),
and K designated hub farms (nodes 1..K), answer Q queries asking for the minimum-cost route
from farm a to farm b that passes through at least one hub (possibly start or end).
Report the number of feasible trips and the sum of their minimum costs.
"""

import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    Q = int(next(it))
    # Initialize distance matrix
    INF = 10**18
    dist = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dist[i][i] = 0
    # Read edges
    for _ in range(M):
        u = int(next(it)); v = int(next(it)); d = int(next(it))
        if d < dist[u][v]:
            dist[u][v] = d

    # Floyd-Warshall all-pairs shortest paths
    for k in range(1, N+1):
        dk = dist[k]
        for i in range(1, N+1):
            di = dist[i]
            via = di[k]
            if via == INF:
                continue
            # Relax paths through k
            for j in range(1, N+1):
                nd = via + dk[j]
                if nd < di[j]:
                    di[j] = nd

    # Process queries
    count = 0
    total_cost = 0
    for _ in range(Q):
        a = int(next(it)); b = int(next(it))
        best = INF
        # Try all hubs
        for h in range(1, K+1):
            da = dist[a][h]
            db = dist[h][b]
            if da < INF and db < INF:
                cost = da + db
                if cost < best:
                    best = cost
        if best < INF:
            count += 1
            total_cost += best

    # Output results
    print(count)
    print(total_cost)

if __name__ == '__main__':
    main()
