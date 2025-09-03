#!/usr/bin/env python3
"""
Solution to 'Roadblock' problem.
"""
import sys
import heapq

def dijkstra(n, adj, edges):
    INF = 10**30
    dist = [INF] * (n + 1)
    prev_edge = [-1] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, ei in adj[u]:
            w = edges[ei][2]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev_edge[v] = ei
                heapq.heappush(heap, (nd, v))
    return dist, prev_edge

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []  # list of (u, v, w)
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Original shortest path
    dist, prev_edge = dijkstra(n, adj, edges)
    orig = dist[n]

    # Reconstruct one shortest path by edges
    path_edges = []
    cur = n
    while cur != 1:
        ei = prev_edge[cur]
        path_edges.append(ei)
        u, v, _ = edges[ei]
        cur = u ^ v ^ cur

    # Try doubling each edge on the path
    max_increase = 0
    for ei in path_edges:
        # double edge weight
        edges[ei][2] *= 2
        new_dist, _ = dijkstra(n, adj, edges)
        # compute increase
        increase = new_dist[n] - orig
        if increase > max_increase:
            max_increase = increase
        # restore weight
        edges[ei][2] //= 2

    print(max_increase)

if __name__ == '__main__':
    main()
