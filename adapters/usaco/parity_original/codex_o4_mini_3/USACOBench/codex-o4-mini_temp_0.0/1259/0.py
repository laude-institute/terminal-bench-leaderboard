#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)

    # Compute core numbers (k-core decomposition)
    deg = [len(adj[u]) for u in range(N)]
    max_deg = max(deg)
    bins = [[] for _ in range(max_deg+1)]
    for u in range(N):
        bins[deg[u]].append(u)
    removed = [False] * N
    core = [0] * N
    # Peel nodes in increasing degree
    for k in range(max_deg+1):
        stack = bins[k]
        while stack:
            u = stack.pop()
            if removed[u] or deg[u] != k:
                continue
            removed[u] = True
            core[u] = k
            for v in adj[u]:
                if not removed[v]:
                    d_old = deg[v]
                    deg[v] -= 1
                    bins[d_old-1].append(v)

    # Prepare DSU for dynamic connectivity
    parent = list(range(N))
    size = [1] * N
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx = find(x); ry = find(y)
        if rx == ry:
            return rx
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx] += size[ry]
        return rx

    # Process nodes in descending core order
    nodes = list(range(N))
    nodes.sort(key=lambda u: core[u], reverse=True)
    added = [False] * N
    ans = 0
    for u in nodes:
        added[u] = True
        for v in adj[u]:
            if added[v]:
                union(u, v)
        ru = find(u)
        comp_sz = size[ru]
        ans = max(ans, core[u] * comp_sz)

    print(ans)

if __name__ == '__main__':
    main()
