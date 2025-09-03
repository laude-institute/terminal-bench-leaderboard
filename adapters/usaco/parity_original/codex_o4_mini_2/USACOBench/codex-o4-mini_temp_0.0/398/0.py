#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    # Store edges and adjacency list
    edges = []  # each entry: [u, v, w]
    adj = [[] for _ in range(N+1)]
    for idx in range(M):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append([u, v, w])
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    INF = 10**30
    # Dijkstra: returns distances, parent node, and parent edge indices
    def dijkstra():
        dist = [INF] * (N+1)
        visited = [False] * (N+1)
        parent_node = [-1] * (N+1)
        parent_edge = [-1] * (N+1)
        dist[1] = 0
        heap = [(0, 1)]
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            if u == N:
                break
            for v, eidx in adj[u]:
                if visited[v]:
                    continue
                w = edges[eidx][2]
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    parent_node[v] = u
                    parent_edge[v] = eidx
                    heapq.heappush(heap, (nd, v))
        return dist, parent_node, parent_edge

    # Initial shortest path
    dist0, parent_node, parent_edge = dijkstra()
    orig_dist = dist0[N]
    # Reconstruct the path from 1 to N
    path_edges = []
    cur = N
    while cur != 1:
        eidx = parent_edge[cur]
        path_edges.append(eidx)
        cur = parent_node[cur]

    # Try doubling each edge on the path
    max_gain = 0
    for eidx in path_edges:
        # double edge weight
        edges[eidx][2] *= 2
        dist1, _, _ = dijkstra()
        gain = dist1[N] - orig_dist
        if gain > max_gain:
            max_gain = gain
        # restore weight
        edges[eidx][2] //= 2

    print(max_gain)

if __name__ == '__main__':
    main()
