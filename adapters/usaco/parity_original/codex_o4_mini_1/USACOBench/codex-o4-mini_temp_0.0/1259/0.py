#!/usr/bin/env python3
"""
Compute the maximum friendship group strength.
"""
import sys

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin
    N, M = map(int, data.readline().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, data.readline().split())
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)

    # Compute core numbers via peeling (min-heap)
    import heapq
    deg = [len(adj[i]) for i in range(N)]
    visited = [False] * N
    core = [0] * N
    heap = [(deg[i], i) for i in range(N)]
    heapq.heapify(heap)
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        core[u] = d
        for v in adj[u]:
            if not visited[v]:
                deg[v] -= 1
                heapq.heappush(heap, (deg[v], v))

    # Process nodes in descending core order, maintain DSU
    nodes = list(range(N))
    nodes.sort(key=lambda u: core[u], reverse=True)
    parent = list(range(N))
    size = [1] * N
    active = [False] * N

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv:
            return
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]

    ans = 0
    for u in nodes:
        active[u] = True
        for v in adj[u]:
            if active[v]:
                union(u, v)
        ru = find(u)
        ans = max(ans, size[ru] * core[u])

    print(ans)

if __name__ == '__main__':
    main()
