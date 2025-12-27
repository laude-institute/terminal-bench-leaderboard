#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    flows = set()
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        f = int(next(it))
        adj[a].append((b, c, f))
        adj[b].append((a, c, f))
        flows.add(f)
    thresholds = sorted(flows, reverse=True)
    best = 0
    INF = 10**18
    for th in thresholds:
        dist = [INF] * (n+1)
        dist[1] = 0
        heap = [(0, 1)]
        while heap:
            cost_u, u = heapq.heappop(heap)
            if cost_u > dist[u]:
                continue
            if u == n:
                break
            for v, c_edge, f_edge in adj[u]:
                if f_edge < th:
                    continue
                nc = cost_u + c_edge
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(heap, (nc, v))
        if dist[n] < INF:
            val = th * 1000000 // dist[n]
            if val > best:
                best = val
    print(best)

if __name__ == "__main__":
    main()
