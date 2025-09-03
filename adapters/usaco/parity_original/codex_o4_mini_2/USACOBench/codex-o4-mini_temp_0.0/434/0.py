#!/usr/bin/env python3
import sys
import heapq

def dijkstra(n, adj):
    INF = 10**30
    dist = [INF] * (n+1)
    dist[n] = 0
    hq = [(0, n)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for w, v in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    revP = [[] for _ in range(n+1)]
    revQ = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, p, q = map(int, input().split())
        edges.append((u, v, p, q))
        revP[v].append((p, u))
        revQ[v].append((q, u))
    dP = dijkstra(n, revP)
    dQ = dijkstra(n, revQ)
    # build complaint cost graph
    graph = [[] for _ in range(n+1)]
    for u, v, p, q in edges:
        c = 0
        if dP[u] != p + dP[v]:
            c += 1
        if dQ[u] != q + dQ[v]:
            c += 1
        graph[u].append((c, v))
    # dijkstra from 1 to n on complaint graph
    INF = 10**30
    dist = [INF] * (n+1)
    dist[1] = 0
    hq = [(0, 1)]
    while hq:
        d, u = heapq.heappop(hq)
        if u == n:
            print(d)
            return
        if d > dist[u]:
            continue
        for w, v in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    print(dist[n])

if __name__ == "__main__":
    main()
