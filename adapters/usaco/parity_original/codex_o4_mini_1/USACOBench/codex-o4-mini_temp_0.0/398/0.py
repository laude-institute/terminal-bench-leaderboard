#!/usr/bin/env python3
"""
USACO Problem: Roadblock
Find the maximum increase in shortest path length when doubling any single edge on the original shortest path.
"""
import sys
import heapq

def dijkstra(N, adj, edges, need_parent=False):
    INF = 10**30
    dist = [INF] * (N + 1)
    dist[1] = 0
    parent_edge = [-1] * (N + 1) if need_parent else None
    parent_node = [-1] * (N + 1) if need_parent else None
    visited = [False] * (N + 1)
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        # early exit if only distances needed
        if u == N and not need_parent:
            break
        for v, eid in adj[u]:
            w = edges[eid][2]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                if need_parent:
                    parent_edge[v] = eid
                    parent_node[v] = u
                heapq.heappush(heap, (nd, v))
    if need_parent:
        return dist, parent_edge, parent_node
    return dist

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edges = []  # list of [u, v, w]
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        adj[u].append((v, i))
        adj[v].append((u, i))

    # initial shortest paths with parent tracking
    dist, parent_edge, parent_node = dijkstra(N, adj, edges, need_parent=True)
    orig = dist[N]

    # reconstruct the edges on the original shortest path
    path_edges = []
    cur = N
    while cur != 1:
        eid = parent_edge[cur]
        path_edges.append(eid)
        cur = parent_node[cur]

    max_inc = 0
    # try doubling each edge on the path
    for eid in path_edges:
        # double weight
        edges[eid][2] *= 2
        new_dist = dijkstra(N, adj, edges, need_parent=False)
        if new_dist[N] < 10**29:
            inc = new_dist[N] - orig
            if inc > max_inc:
                max_inc = inc
        # restore original weight
        edges[eid][2] //= 2

    print(max_inc)

if __name__ == '__main__':
    main()
