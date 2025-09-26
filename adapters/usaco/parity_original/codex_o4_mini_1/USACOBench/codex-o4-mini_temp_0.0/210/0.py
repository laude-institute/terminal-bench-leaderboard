#!/usr/bin/env python3
"""
Milk Routing solution: finds the path from node 1 to N minimizing latency + X/capacity.
"""
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    X = int(next(it))
    edges = []
    caps = set()
    for _ in range(M):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        L = int(next(it))
        C = int(next(it))
        edges.append((u, v, L, C))
        caps.add(C)

    caps = sorted(caps)
    INF = 10**30
    best_num = INF
    best_den = 1

    # For each possible capacity, find shortest latency path using edges with cap>=C
    for C in caps:
        adj = [[] for _ in range(N)]
        for u, v, L, c in edges:
            if c >= C:
                adj[u].append((v, L))
                adj[v].append((u, L))

        # Dijkstra
        dist = [INF] * N
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        dN = dist[N-1]
        if dN >= INF:
            continue

        # total time = dN + X/C => compare fractions to avoid float
        num = dN * C + X
        den = C
        # compare num/den < best_num/best_den => num * best_den < best_num * den
        if num * best_den < best_num * den:
            best_num = num
            best_den = den

    # print floor of best fraction
    print(best_num // best_den)

if __name__ == '__main__':
    main()
