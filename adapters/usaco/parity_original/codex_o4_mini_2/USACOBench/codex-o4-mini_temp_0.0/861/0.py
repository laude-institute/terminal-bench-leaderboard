#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    import heapq

    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        adj[a].append((b, t))
        adj[b].append((a, t))

    # Compute shortest distances to barn (node N)
    INF = 10**30
    dist_to_barn = [INF] * (N+1)
    dist_to_barn[N] = 0
    pq = [(0, N)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist_to_barn[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist_to_barn[v]:
                dist_to_barn[v] = nd
                heapq.heappush(pq, (nd, v))

    # Prepare multi-source Dijkstra from haybales
    # initial cost at hay pasture h is p[h] = dist_to_barn[h] - y
    best = [INF] * (N+1)
    pq = []
    for _ in range(K):
        h, y = map(int, input().split())
        cost = dist_to_barn[h] - y
        if cost < best[h]:
            best[h] = cost
            heapq.heappush(pq, (cost, h))

    # Run Dijkstra to compute best[i] = min_h(dist(i,h) + p[h])
    while pq:
        c, u = heapq.heappop(pq)
        if c != best[u]:
            continue
        for v, w in adj[u]:
            nc = c + w
            if nc < best[v]:
                best[v] = nc
                heapq.heappush(pq, (nc, v))

    # For each cow at pasture 1..N-1, check if best[i] <= dist_to_barn[i]
    out = []
    for i in range(1, N):
        out.append('1' if best[i] <= dist_to_barn[i] else '0')
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
