#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj, edges):
    dist = [float('inf')] * (n + 1)
    parent_edge = [-1] * (n + 1)
    dist[1] = 0
    hq = [(0, 1)]  # (distance, node)
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, ei in adj[u]:
            w = edges[ei][2]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent_edge[v] = ei
                heapq.heappush(hq, (nd, v))
    return dist, parent_edge

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    edges = []  # list of [u, v, w]
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for ei in range(m):
        u = int(data[idx]); v = int(data[idx+1]); w = int(data[idx+2])
        idx += 3
        edges.append([u, v, w])
        adj[u].append((v, ei))
        adj[v].append((u, ei))

    # compute original shortest path
    dist0, parent_edge = dijkstra(n, adj, edges)
    orig = dist0[n]

    # reconstruct path edge indices
    path_edges = []
    cur = n
    while cur != 1:
        ei = parent_edge[cur]
        path_edges.append(ei)
        u, v, _ = edges[ei]
        cur = u ^ v ^ cur  # go to the other node

    # try doubling each edge on the path
    best = 0
    for ei in path_edges:
        # double weight
        edges[ei][2] *= 2
        dist_new, _ = dijkstra(n, adj, edges)
        if dist_new[n] < float('inf'):
            best = max(best, dist_new[n] - orig)
        # revert weight
        edges[ei][2] //= 2

    print(best)

if __name__ == '__main__':
    main()
