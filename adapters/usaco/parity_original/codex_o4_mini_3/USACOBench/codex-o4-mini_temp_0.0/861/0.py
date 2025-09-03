#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin
    INF = 10**30
    # read input
    N, M, K = map(int, data.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, t = map(int, data.readline().split())
        graph[a].append((b, t))
        graph[b].append((a, t))
    haybales = []
    for _ in range(K):
        p, y = map(int, data.readline().split())
        haybales.append((p, y))

    # Dijkstra from barn (node N) to compute shortest paths distN
    distN = [INF] * (N+1)
    distN[N] = 0
    heap = [(0, N)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > distN[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < distN[v]:
                distN[v] = nd
                heapq.heappush(heap, (nd, v))

    # initialize best extra-cost from haybales
    best = [INF] * (N+1)
    for p, y in haybales:
        cost = distN[p] - y
        if cost < best[p]:
            best[p] = cost

    # multi-source Dijkstra to propagate best costs
    heap = [(best[i], i) for i in range(1, N+1) if best[i] < INF]
    heapq.heapify(heap)
    while heap:
        d, u = heapq.heappop(heap)
        if d > best[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < best[v]:
                best[v] = nd
                heapq.heappush(heap, (nd, v))

    # output results for cows at 1..N-1
    out = []
    for i in range(1, N):
        out.append('1' if best[i] <= distN[i] else '0')
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
