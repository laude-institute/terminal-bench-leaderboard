#!/usr/bin/env python3
import sys

def min_cost_max_flow(n, graph, src, sink):
    N = len(graph)
    flow = 0
    cost = 0
    INF = 10**18
    # While we can send more flow
    while True:
        dist = [INF] * N
        in_queue = [False] * N
        prev_node = [-1] * N
        prev_edge = [-1] * N
        dist[src] = 0
        from collections import deque
        q = deque([src])
        in_queue[src] = True
        # SPFA
        while q:
            u = q.popleft()
            in_queue[u] = False
            for i, e in enumerate(graph[u]):
                if e['cap'] > 0 and dist[e['to']] > dist[u] + e['cost']:
                    dist[e['to']] = dist[u] + e['cost']
                    prev_node[e['to']] = u
                    prev_edge[e['to']] = i
                    if not in_queue[e['to']]:
                        in_queue[e['to']] = True
                        q.append(e['to'])
        if dist[sink] == INF:
            break
        # find max flow on that path
        f = INF
        v = sink
        while v != src:
            u = prev_node[v]
            e = graph[u][prev_edge[v]]
            f = min(f, e['cap'])
            v = u
        # apply flow
        v = sink
        while v != src:
            u = prev_node[v]
            e = graph[u][prev_edge[v]]
            e['cap'] -= f
            graph[v][e['rev']]['cap'] += f
            v = u
        flow += f
        cost += f * dist[sink]
    return flow, cost

def add_edge(graph, u, v, cap, cost):
    graph[u].append({'to': v, 'cap': cap, 'cost': cost, 'rev': len(graph[v])})
    graph[v].append({'to': u, 'cap': 0, 'cost': -cost, 'rev': len(graph[u]) - 1})

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    X = int(next(it))
    Y = int(next(it))
    Z = int(next(it))
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i] = int(next(it))
        B[i] = int(next(it))
    # nodes 0..N-1, src=N, sink=N+1
    src = N
    sink = N + 1
    size = N + 2
    graph = [[] for _ in range(size)]
    # build
    for i in range(N):
        diff = A[i] - B[i]
        if diff > 0:
            # supply: remove or transport
            add_edge(graph, src, i, diff, 0)
            add_edge(graph, i, sink, diff, Y)
        elif diff < 0:
            # demand: purchase or transport
            add_edge(graph, src, i, -diff, X)
            add_edge(graph, i, sink, -diff, 0)
    # transport edges
    INF_CAP = sum(max(0, A[i] - B[i]) for i in range(N))
    INF_CAP += sum(max(0, B[i] - A[i]) for i in range(N))
    for i in range(N):
        for j in range(N):
            # allow moving any amount
            add_edge(graph, i, j, INF_CAP, Z * abs(i - j))
    # compute min-cost max-flow
    _, result = min_cost_max_flow(N, graph, src, sink)
    print(result)

if __name__ == '__main__':
    main()
