#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    idx = 2
    # DSU for 'same' constraints
    parent = list(range(N))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    diff_edges = []
    # process constraints
    for _ in range(K):
        t = data[idx]; x = int(data[idx+1]) - 1; y = int(data[idx+2]) - 1
        idx += 3
        if t == 'S':
            union(x, y)
        else:
            diff_edges.append((x, y))

    # compress parents
    for i in range(N):
        parent[i] = find(i)
    # map each component to an index
    roots = sorted(set(parent))
    comp_index = {r: i for i, r in enumerate(roots)}
    M = len(roots)

    # build graph of 'different' constraints among components
    adj = [set() for _ in range(M)]
    for x, y in diff_edges:
        rx = comp_index[parent[x]]
        ry = comp_index[parent[y]]
        # contradiction if same component must differ
        if rx == ry:
            print(0)
            return
        adj[rx].add(ry)
        adj[ry].add(rx)

    visited = [False] * M

    def count_cc(nodes):
        # backtracking color count for one connected component
        assign = {}
        def dfs(i):
            if i == len(nodes):
                return 1
            u = nodes[i]
            total = 0
            for c in range(3):
                ok = True
                for v in adj[u]:
                    if v in assign and assign[v] == c:
                        ok = False
                        break
                if not ok:
                    continue
                assign[u] = c
                total += dfs(i + 1)
                del assign[u]
            return total
        return dfs(0)

    result = 1
    # for each connected component in diff-graph, multiply possibilities
    for i in range(M):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            cc = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        cc.append(v)
            result *= count_cc(cc)

    print(result)

if __name__ == '__main__':
    main()
