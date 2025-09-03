#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj, edges):
    dist = [float('inf')] * (n + 1)
    parent = [(-1, -1)] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, idx in adj[u]:
            w = edges[idx][2]
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = (u, idx)
                heapq.heappush(heap, (nd, v))
    return dist, parent

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        adj[u].append((v, i))
        adj[v].append((u, i))

    # initial shortest path
    dist, parent = dijkstra(n, adj, edges)
    original = dist[n]

    # reconstruct path edges from 1 to n
    path_edges = []
    cur = n
    while cur != 1:
        u, idx = parent[cur]
        path_edges.append(idx)
        cur = u

    max_inc = 0
    # try doubling each edge on the shortest path
    for idx in path_edges:
        # double edge weight
        edges[idx][2] *= 2
        dist2, _ = dijkstra(n, adj, edges)
        max_inc = max(max_inc, dist2[n] - original)
        # restore edge weight
        edges[idx][2] //= 2

    print(max_inc)

if __name__ == '__main__':
    main()
