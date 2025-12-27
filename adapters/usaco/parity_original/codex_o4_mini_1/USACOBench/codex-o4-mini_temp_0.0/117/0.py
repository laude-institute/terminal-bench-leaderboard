#!/usr/bin/env python3
import sys
import heapq

def dijkstra(start, adj, n):
    dist = [float('inf')] * (n + 1)
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
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    markets = [int(input()) for _ in range(K)]
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Compute distances from each market to all towns
    dist_from = []
    for m in markets:
        dist_from.append(dijkstra(m, adj, N))

    # Precompute distances between markets
    dist_market = [[0]*K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            dist_market[i][j] = dist_from[i][markets[j]]

    import itertools
    result = float('inf')
    markets_set = set(markets)
    # For each possible farm location
    for v in range(1, N+1):
        if v in markets_set:
            continue
        # Try all orders to visit markets
        best_for_v = float('inf')
        for perm in itertools.permutations(range(K)):
            cost = dist_from[perm[0]][v]
            for i in range(K-1):
                cost += dist_market[perm[i]][perm[i+1]]
            cost += dist_from[perm[-1]][v]
            if cost < best_for_v:
                best_for_v = cost
        if best_for_v < result:
            result = best_for_v

    print(result)

if __name__ == '__main__':
    main()
