#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    flows = set()
    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        c = int(next(it)); f = int(next(it))
        adj[a].append((b, c, f))
        adj[b].append((a, c, f))
        flows.add(f)
    # Evaluate best ratio = F / cost
    best_f = 0
    best_c = 1
    # Test each possible flow threshold
    for F in sorted(flows):
        # Dijkstra on edges with flow >= F
        dist = [10**18] * (n+1)
        dist[1] = 0
        pq = [(0, 1)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n:
                break
            for v, cost, f_edge in adj[u]:
                if f_edge < F:
                    continue
                nd = d + cost
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        cN = dist[n]
        if cN == 10**18:
            continue
        # Compare F/cN > best_f/best_c  <=> F*best_c > best_f*cN
        if best_f * cN < F * best_c:
            best_f = F
            best_c = cN
    # Output scaled ratio
    result = best_f * 1000000 // best_c
    print(result)

if __name__ == '__main__':
    main()
