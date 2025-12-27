#!/usr/bin/env python3
import sys

def main():
    sys.setrecursionlimit(300000)
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, M = map(int, input().split())
    parent = list(range(N+1))
    # DSU functions
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra

    edges = []  # list of edges
    deg = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1
        union(u, v)

    # Count nodes and edges per component
    comp_nodes = {}
    comp_edges = {}
    members = {}
    for i in range(1, N+1):
        r = find(i)
        comp_nodes[r] = comp_nodes.get(r, 0) + 1
        members.setdefault(r, []).append(i)
    for u, v in edges:
        r = find(u)
        comp_edges[r] = comp_edges.get(r, 0) + 1

    result = 1
    for r, nodes in comp_nodes.items():
        m = comp_edges.get(r, 0)
        if m > nodes:
            print(0)
            return
        if m == nodes - 1:
            # tree component: ways = number of nodes
            result = result * nodes % MOD
        elif m == nodes:
            # should be a simple cycle: all degrees == 2
            ok = True
            for x in members[r]:
                if deg[x] != 2:
                    ok = False
                    break
            if not ok:
                print(0)
                return
            result = result * 2 % MOD
        else:
            # isolated node or impossible
            # for m == 0 and nodes == 1, nodes-1 == 0 handled above
            # other cases m < nodes-1 impossible
            if m == 0 and nodes == 1:
                continue
            print(0)
            return
    print(result)

if __name__ == '__main__':
    main()
