#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    # Read preferences and build rank table
    prefs = [None] * (n + 1)
    rank = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        prefs[i] = [0] * n
        for j in range(n):
            g = int(next(it))
            prefs[i][j] = g
            rank[i][g] = j

    # Build graph: cow i -> cow j if i prefers gift j over its original gift i
    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    outdeg = [0] * (n + 1)
    for i in range(1, n + 1):
        orig = i
        for g in prefs[i]:
            if rank[i][g] < rank[i][orig]:
                graph[i].append(g)
        outdeg[i] = len(graph[i])
        for j in graph[i]:
            rev[j].append(i)

    # Iteratively prune cows with no outgoing edges
    from collections import deque
    alive = [True] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if outdeg[i] == 0:
            alive[i] = False
            q.append(i)
    while q:
        u = q.popleft()
        for v in rev[u]:
            if not alive[v]:
                continue
            outdeg[v] -= 1
            if outdeg[v] == 0:
                alive[v] = False
                q.append(v)

    # Build subgraph of alive nodes for SCC
    g2 = [[] for _ in range(n + 1)]
    gr2 = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not alive[i]:
            continue
        for j in graph[i]:
            if alive[j]:
                g2[i].append(j)
                gr2[j].append(i)

    # Kosaraju's algorithm
    sys.setrecursionlimit(10000)
    visited = [False] * (n + 1)
    order = []
    def dfs(u):
        visited[u] = True
        for v in g2[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)
    for i in range(1, n + 1):
        if alive[i] and not visited[i]:
            dfs(i)

    comp = [0] * (n + 1)
    cid = 0
    def dfs2(u):
        comp[u] = cid
        for v in gr2[u]:
            if comp[v] == 0:
                dfs2(v)
    for u in reversed(order):
        if comp[u] == 0:
            cid += 1
            dfs2(u)

    # Count component sizes
    comp_size = [0] * (cid + 1)
    for i in range(1, n + 1):
        if alive[i]:
            comp_size[comp[i]] += 1

    # Compute answers
    out = []
    for i in range(1, n + 1):
        if alive[i] and comp_size[comp[i]] > 1:
            # Choose best gift among cows in same SCC
            best = i
            for g in prefs[i]:
                if alive[g] and comp[g] == comp[i]:
                    best = g
                    break
            out.append(str(best))
        else:
            out.append(str(i))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
