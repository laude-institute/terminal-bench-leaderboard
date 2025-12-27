#!/usr/bin/env python3
import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    # Read market towns (0-indexed)
    markets = [int(input().strip()) - 1 for _ in range(K)]
    # Build adjacency list
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Compute shortest paths from each market to all towns
    dists = [[float('inf')] * N for _ in range(K)]
    for i, src in enumerate(markets):
        dist = dists[i]
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d_u, u = heapq.heappop(heap)
            if d_u > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d_u + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

    # Precompute inter-market distances
    m2m = [[0] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            m2m[i][j] = dists[i][markets[j]]

    market_set = set(markets)
    ans = float('inf')
    # Try each non-market town as farm location
    from itertools import permutations
    for farm in range(N):
        if farm in market_set:
            continue
        best = float('inf')
        # Evaluate all orders to visit markets
        for perm in permutations(range(K)):
            total = dists[perm[0]][farm]
            for x in range(K - 1):
                total += m2m[perm[x]][perm[x + 1]]
            total += dists[perm[-1]][farm]
            if total < best:
                best = total
        if best < ans:
            ans = best

    print(ans)

if __name__ == '__main__':
    main()
