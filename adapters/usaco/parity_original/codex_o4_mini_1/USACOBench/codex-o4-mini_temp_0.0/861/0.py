#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin
    N, M, K = map(int, data.readline().split())
    # Build graph
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, t = map(int, data.readline().split())
        adj[a].append((b, t))
        adj[b].append((a, t))
    # Shortest distances from each node to barn (node N)
    INF = 10**30
    dist = [INF] * (N+1)
    dist[N] = 0
    pq = [(0, N)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    # Read haybales and record best yumminess per pasture
    best_y = [0] * (N+1)
    for _ in range(K):
        b, y = map(int, data.readline().split())
        if y > best_y[b]:
            best_y[b] = y
    # Multi-source Dijkstra: initial cost = dist[b] - best_y[b]
    dh = [INF] * (N+1)
    pq = []
    for b in range(1, N+1):
        if best_y[b] > 0:
            init = dist[b] - best_y[b]
            dh[b] = init
            heapq.heappush(pq, (init, b))
    while pq:
        d, u = heapq.heappop(pq)
        if d > dh[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dh[v]:
                dh[v] = nd
                heapq.heappush(pq, (nd, v))
    # For each cow at 1..N-1, check if can dine
    out = []
    for i in range(1, N):
        out.append('1' if dh[i] <= dist[i] else '0')
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    main()
