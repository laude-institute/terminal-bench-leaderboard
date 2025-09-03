#!/usr/bin/env python3
import sys
import heapq

"""
1. Restatement:
   Given a network of N junctions and M bi-directional pipes, each with a latency L and capacity C,
   find a single path from junction 1 to junction N that minimizes total time to send X units of milk,
   where time = sum(latencies) + X / min(capacities) along the path.

2. Conceptualization:
   We can iterate over each possible bottleneck capacity c present in the pipes. For each c,
   consider only pipes with capacity >= c, and compute the shortest path latency from 1 to N via Dijkstra.
   Then total time = latency + X / c. Track the minimum over all c.

3. Pseudocode:
   read N, M, X
   read list of edges (u, v, L, C)
   capacities = sorted unique C values
   best_time = infinity
   for c in capacities:
       build graph using edges with C >= c
       compute shortest latency from 1 to N via Dijkstra
       if reachable:
           time = latency + X / c
           update best_time
   print floor(best_time)
"""

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    X = int(next(it))
    edges = []
    capacities = set()
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        L = int(next(it))
        C = int(next(it))
        edges.append((u-1, v-1, L, C))
        capacities.add(C)

    capacities = sorted(capacities)
    INF = float('inf')
    best_time = INF

    # Iterate over possible bottleneck capacities
    for c in capacities:
        # build graph adjacency list
        adj = [[] for _ in range(N)]
        for u, v, L, C in edges:
            if C >= c:
                adj[u].append((v, L))
                adj[v].append((u, L))
        # Dijkstra for latency
        dist = [INF] * N
        dist[0] = 0
        hq = [(0, 0)]  # (distance, node)
        while hq:
            d, node = heapq.heappop(hq)
            if d > dist[node]:
                continue
            if node == N-1:
                break
            for nei, w in adj[node]:
                nd = d + w
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(hq, (nd, nei))
        # if reachable, compute time
        if dist[N-1] < INF:
            time = dist[N-1] + X / c
            if time < best_time:
                best_time = time

    # output floor of best_time
    # convert to int via flooring
    print(int(best_time))

if __name__ == '__main__':
    main()
