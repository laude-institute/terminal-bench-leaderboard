#!/usr/bin/env python3
"""
Solution for Dueling GPSs problem (gpsduel).
Compute shortest distances to target under both GPS metrics,
then find minimal complaint path from source using Dijkstra.
"""
import sys
import heapq

def dijkstra(graph, start, n):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    rev1 = [[] for _ in range(n + 1)]
    rev2 = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, p, q = map(int, input().split())
        edges.append((u, v, p, q))
        rev1[v].append((u, p))
        rev2[v].append((u, q))

    # Shortest distances to target under each GPS metric
    d1 = dijkstra(rev1, n, n)
    d2 = dijkstra(rev2, n, n)

    # Build graph with complaint costs
    adj = [[] for _ in range(n + 1)]
    for u, v, p, q in edges:
        cost = 0
        if p + d1[v] != d1[u]:
            cost += 1
        if q + d2[v] != d2[u]:
            cost += 1
        adj[u].append((v, cost))

    # Dijkstra from source to compute minimal complaints
    dist = [10**18] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == n:
            break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    print(dist[n])

if __name__ == '__main__':
    main()
