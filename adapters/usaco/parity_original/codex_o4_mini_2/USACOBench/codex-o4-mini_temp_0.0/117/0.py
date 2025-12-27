#!/usr/bin/env python3
import sys
import heapq
import itertools

def dijkstra(start, adj, n):
    """Compute shortest paths from start to all nodes."""
    INF = 10**18
    dist = [INF] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    # Read market towns (0-indexed)
    markets = [int(next(it)) - 1 for _ in range(k)]
    market_set = set(markets)

    # Build graph
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Compute distances from each market to all towns
    dist_matrix = [dijkstra(src, adj, n) for src in markets]

    # Precompute distances between markets
    market_dist = [[0]*k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            market_dist[i][j] = dist_matrix[i][markets[j]]

    INF = 10**18
    best = INF

    # Try each non-market town as farm location
    for f in range(n):
        if f in market_set:
            continue
        # distances from farm to each market
        df = [dist_matrix[i][f] for i in range(k)]
        # Try all visit orders of markets
        for perm in itertools.permutations(range(k)):
            total = df[perm[0]]
            # between markets
            for i in range(k-1):
                total += market_dist[perm[i]][perm[i+1]]
            total += df[perm[-1]]
            if total < best:
                best = total

    # Output the minimal travel distance
    print(best)

if __name__ == '__main__':
    main()
