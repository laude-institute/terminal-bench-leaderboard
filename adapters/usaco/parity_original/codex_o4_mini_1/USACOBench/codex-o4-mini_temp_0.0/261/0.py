#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    # DSU for same-breed constraints
    parent = list(range(N+1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    diff_constraints = []
    # Read constraints
    for _ in range(K):
        typ = next(it)
        x = int(next(it))
        y = int(next(it))
        if typ == 'S':
            union(x, y)
        else:  # 'D'
            diff_constraints.append((x, y))

    # Check for conflicts in diff constraints
    for x, y in diff_constraints:
        if find(x) == find(y):
            print(0)
            return

    # Map each component root to an index
    roots = {}
    idx = 0
    for i in range(1, N+1):
        r = find(i)
        if r not in roots:
            roots[r] = idx
            idx += 1
    M = idx

    # Build graph of diff edges between components
    graph = [[] for _ in range(M)]
    for x, y in diff_constraints:
        u = roots[find(x)]
        v = roots[find(y)]
        graph[u].append(v)
        graph[v].append(u)

    # Count 3-colorings with backtracking
    colors = [-1] * M
    count = 0

    def dfs(pos):
        nonlocal count
        if pos == M:
            count += 1
            return
        for col in range(3):
            ok = True
            for nei in graph[pos]:
                if nei < pos and colors[nei] == col:
                    ok = False
                    break
            if not ok:
                continue
            colors[pos] = col
            dfs(pos+1)
            colors[pos] = -1

    dfs(0)
    print(count)


if __name__ == '__main__':
    main()
