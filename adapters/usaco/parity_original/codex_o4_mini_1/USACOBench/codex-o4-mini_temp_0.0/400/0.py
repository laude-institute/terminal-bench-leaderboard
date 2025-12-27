#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj, edges):
    dist = [float('inf')] * (n + 1)
    parent_edge = [-1] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for idx in adj[u]:
            a, b, w = edges[idx]
            v = b if u == a else a
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent_edge[v] = idx
                heapq.heappush(heap, (nd, v))
    return dist, parent_edge

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []  # list of [u, v, w]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, l = map(int, input().split())
        edges.append([a, b, l])
        adj[a].append(i)
        adj[b].append(i)

    # original shortest path
    dist0, parent_edge = dijkstra(n, adj, edges)
    orig_dist = dist0[n]

    # reconstruct the edges on the shortest path from 1 to n
    path_edges = []
    v = n
    while v != 1:
        idx = parent_edge[v]
        path_edges.append(idx)
        u, w = edges[idx][0], edges[idx][1]
        v = w if v == u else u

    # test doubling each edge on the path
    max_increase = 0
    for idx in path_edges:
        # double weight
        orig_w = edges[idx][2]
        edges[idx][2] = orig_w * 2
        dist_new, _ = dijkstra(n, adj, edges)
        if dist_new[n] < float('inf'):
            max_increase = max(max_increase, dist_new[n] - orig_dist)
        # restore
        edges[idx][2] = orig_w

    print(max_increase)

if __name__ == '__main__':
    main()
