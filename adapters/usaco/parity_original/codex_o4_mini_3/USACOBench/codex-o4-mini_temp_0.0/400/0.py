#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj, edges):
    INF = 10**30
    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, eid in adj[u]:
            w = edges[eid][2]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                parent_edge[v] = eid
                heapq.heappush(heap, (nd, v))
    return dist, prev, parent_edge

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n + 1)]
    for eid in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # initial shortest paths
    dist0, prev, parent_edge = dijkstra(n, adj, edges)
    original = dist0[n]
    # reconstruct path from n to 1
    path_edges = []
    curr = n
    while curr != 1:
        eid = parent_edge[curr]
        path_edges.append(eid)
        curr = prev[curr]

    # try doubling each edge on the path
    best_increase = 0
    for eid in path_edges:
        # double the edge weight
        u, v, w = edges[eid]
        edges[eid][2] = w * 2
        dist1, _, _ = dijkstra(n, adj, edges)
        best_increase = max(best_increase, dist1[n] - original)
        # restore original weight
        edges[eid][2] = w

    print(best_increase)

if __name__ == '__main__':
    main()
