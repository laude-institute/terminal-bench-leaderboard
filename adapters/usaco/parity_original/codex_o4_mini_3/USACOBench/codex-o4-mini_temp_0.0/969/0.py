#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    # adjacency list: node -> list of (neighbor, cost, flow)
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

    # function to compute shortest path cost from 1 to n using only edges with flow>=minf
    def dijkstra(minf):
        INF = 10**18
        dist = [INF] * (n+1)
        dist[1] = 0
        hq = [(0, 1)]  # (dist, node)
        while hq:
            d, u = heapq.heappop(hq)
            if d > dist[u]:
                continue
            if u == n:
                break
            for v, cost, flow in adj[u]:
                if flow < minf:
                    continue
                nd = d + cost
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd, v))
        return dist[n]

    best = 0
    # check each possible flow threshold
    for f in sorted(flows, reverse=True):
        cost = dijkstra(f)
        if cost == 10**18 or cost <= 0:
            continue
        # compute scaled ratio (floor of f*1e6/cost)
        val = (f * 1000000) // cost
        if val > best:
            best = val
    # output best found
    print(best)

if __name__ == '__main__':
    main()
