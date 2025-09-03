#!/usr/bin/env python3
import sys
import heapq

class Edge:
    def __init__(self, to, cap, cost, rev):
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev

def add_edge(graph, fr, to, cap, cost):
    graph[fr].append(Edge(to, cap, cost, len(graph[to])))
    graph[to].append(Edge(fr, 0, -cost, len(graph[fr]) - 1))

def min_cost_flow(graph, s, t, maxf):
    n = len(graph)
    prevv = [0] * n
    preve = [0] * n
    INF = 10**18
    res = 0
    h = [0] * n  # potential
    dist = [0] * n
    flow = 0
    while flow < maxf:
        dist = [INF] * n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, v = heapq.heappop(pq)
            if dist[v] < d:
                continue
            for i, e in enumerate(graph[v]):
                if e.cap > 0 and dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]:
                    dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                    prevv[e.to] = v
                    preve[e.to] = i
                    heapq.heappush(pq, (dist[e.to], e.to))
        if dist[t] == INF:
            # cannot flow more
            break
        for v in range(n):
            if dist[v] < INF:
                h[v] += dist[v]
        d = maxf - flow
        v = t
        while v != s:
            d = min(d, graph[prevv[v]][preve[v]].cap)
            v = prevv[v]
        flow += d
        res += d * h[t]
        v = t
        while v != s:
            e = graph[prevv[v]][preve[v]]
            e.cap -= d
            graph[v][e.rev].cap += d
            v = prevv[v]
    return res

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    X = int(next(it))
    Y = int(next(it))
    Z = int(next(it))
    A = []
    B = []
    for _ in range(N):
        A.append(int(next(it)))
        B.append(int(next(it)))
    # Compute net surplus and deficit
    supply = [max(0, A[i] - B[i]) for i in range(N)]
    demand = [max(0, B[i] - A[i]) for i in range(N)]
    sum_supply = sum(supply)
    sum_demand = sum(demand)
    # build graph: nodes 0=src, 1..N supply, N+1..2N demand, 2N+1 sink
    S = 0
    T = 2 * N + 1
    size = T + 1
    graph = [[] for _ in range(size)]
    # source to supply nodes
    for i in range(N):
        if supply[i] > 0:
            add_edge(graph, S, 1 + i, supply[i], 0)
    # demand nodes to sink
    for j in range(N):
        if demand[j] > 0:
            add_edge(graph, N + 1 + j, T, demand[j], 0)
    # supply to demand transport
    for i in range(N):
        if supply[i] <= 0:
            continue
        for j in range(N):
            if demand[j] <= 0:
                continue
            cost = Z * abs(i - j)
            # only add if transport cheaper than remove+add
            if cost < X + Y:
                add_edge(graph, 1 + i, N + 1 + j, 10**9, cost)
    # supply removal
    for i in range(N):
        if supply[i] > 0:
            add_edge(graph, 1 + i, T, supply[i], Y)
    # purchase for demand
    for j in range(N):
        if demand[j] > 0:
            add_edge(graph, S, N + 1 + j, demand[j], X)
    # max flow = sum_supply + sum_demand
    flow_needed = sum_supply + sum_demand
    result = min_cost_flow(graph, S, T, flow_needed)
    print(result)

if __name__ == '__main__':
    main()
