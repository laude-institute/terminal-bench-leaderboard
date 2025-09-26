#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj, start):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # Store edges and reverse graphs for two weights
    edges = []
    revP = [[] for _ in range(N+1)]
    revQ = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, p, q = map(int, input().split())
        edges.append((u, v, p, q))
        revP[v].append((u, p))
        revQ[v].append((u, q))

    # shortest distances to N under P and Q
    distP = dijkstra(N, revP, N)
    distQ = dijkstra(N, revQ, N)

    # build complaint-weighted graph
    adj = [[] for _ in range(N+1)]
    for u, v, p, q in edges:
        cost = 0
        # if not on any shortest path under P
        if distP[u] != distP[v] + p:
            cost += 1
        # if not on any shortest path under Q
        if distQ[u] != distQ[v] + q:
            cost += 1
        adj[u].append((v, cost))

    # find min complaints from 1 to N
    dist = dijkstra(N, adj, 1)
    print(dist[N])

if __name__ == '__main__':
    main()
