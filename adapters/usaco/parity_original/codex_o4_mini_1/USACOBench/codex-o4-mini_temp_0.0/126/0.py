#!/usr/bin/env python3
import sys

class Edge:
    def __init__(self, to, rev, cap, cost):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.cost = cost

class MinCostMaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, frm, to, cap, cost):
        self.graph[frm].append(Edge(to, len(self.graph[to]), cap, cost))
        self.graph[to].append(Edge(frm, len(self.graph[frm]) - 1, 0, -cost))

    def flow(self, s, t, maxf):
        n = self.n
        prevv = [0] * n
        preve = [0] * n
        INF = 10**18
        res = 0
        h = [0] * n  # potential
        dist = [0] * n
        flow = 0
        import heapq
        while flow < maxf:
            # Dijkstra
            for i in range(n): dist[i] = INF
            dist[s] = 0
            pq = [(0, s)]
            while pq:
                d, v = heapq.heappop(pq)
                if dist[v] < d: continue
                for i, e in enumerate(self.graph[v]):
                    if e.cap > 0 and dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]:
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        prevv[e.to] = v
                        preve[e.to] = i
                        heapq.heappush(pq, (dist[e.to], e.to))
            if dist[t] == INF:
                break
            for v in range(n): h[v] += dist[v]
            # add as much as possible
            d = maxf - flow
            v = t
            while v != s:
                d = min(d, self.graph[prevv[v]][preve[v]].cap)
                v = prevv[v]
            flow += d
            res += d * h[t]
            v = t
            while v != s:
                e = self.graph[prevv[v]][preve[v]]
                e.cap -= d
                self.graph[v][e.rev].cap += d
                v = prevv[v]
        return res

def main():
    data = sys.stdin.read().split()
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
    net = [A[i] - B[i] for i in range(N)]
    # nodes 0..N-1: flowerbeds; N: source; N+1: sink
    s = N
    t = N + 1
    mcmf = MinCostMaxFlow(N + 2)
    total_flow = 0
    # supply and demand edges
    for i in range(N):
        if net[i] > 0:
            # supply
            mcmf.add_edge(s, i, net[i], 0)
            mcmf.add_edge(i, t, net[i], Y)
            total_flow += net[i]
        elif net[i] < 0:
            # demand
            mcmf.add_edge(s, i, -net[i], X)
            mcmf.add_edge(i, t, -net[i], 0)
            total_flow += -net[i]
    # transport edges from supply to demand
    for i in range(N):
        if net[i] <= 0: continue
        for j in range(N):
            if net[j] >= 0: continue
            dist = abs(i - j)
            # capacity at most supply
            mcmf.add_edge(i, j, net[i], Z * dist)
    ans = mcmf.flow(s, t, total_flow)
    print(ans)

if __name__ == '__main__':
    main()
