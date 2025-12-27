#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj, edges):
    dist = [float('inf')] * (n + 1)
    parent_edge = [-1] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, eid in adj[u]:
            w = edges[eid][2]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent_edge[v] = eid
                heapq.heappush(pq, (nd, v))
    return dist, parent_edge

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []  # list of [u, v, w]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Original shortest path
    dist, parent_edge = dijkstra(n, adj, edges)
    orig = dist[n]

    # Reconstruct path edge IDs
    path_edges = []
    cur = n
    while cur != 1:
        eid = parent_edge[cur]
        path_edges.append(eid)
        u, v, _ = edges[eid]
        cur = u ^ v ^ cur

    max_diff = 0
    # Try doubling each edge on the path
    for eid in path_edges:
        # double weight
        edges[eid][2] *= 2
        new_dist, _ = dijkstra(n, adj, edges)
        if new_dist[n] < float('inf'):
            diff = new_dist[n] - orig
            if diff > max_diff:
                max_diff = diff
        # restore weight
        edges[eid][2] //= 2

    print(max_diff)

if __name__ == '__main__':
    main()
