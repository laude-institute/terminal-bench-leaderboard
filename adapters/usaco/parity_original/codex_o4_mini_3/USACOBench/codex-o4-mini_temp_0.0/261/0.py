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
    parent = list(range(N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    diffs = []  # list of (x, y) for different constraints
    for _ in range(K):
        t = next(it)
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        if t == 'S':
            union(x, y)
        else:
            diffs.append((x, y))
    # Check for contradictions: same and different in same comp
    for x, y in diffs:
        if find(x) == find(y):
            print(0)
            return
    # Map each component to an index
    comp_map = {}
    comp_list = []
    for i in range(N):
        r = find(i)
        if r not in comp_map:
            comp_map[r] = len(comp_list)
            comp_list.append(r)
    C = len(comp_list)
    # Build adjacency for different constraints between components
    adj = [[] for _ in range(C)]
    seen = set()
    for x, y in diffs:
        cx = comp_map[find(x)]
        cy = comp_map[find(y)]
        if cx != cy and (cx, cy) not in seen:
            seen.add((cx, cy))
            seen.add((cy, cx))
            adj[cx].append(cy)
            adj[cy].append(cx)

    # Backtracking to count 3-colorings
    count = 0
    colors = [None] * C

    def dfs(u):
        nonlocal count
        if u == C:
            count += 1
            return
        for col in range(3):
            ok = True
            for v in adj[u]:
                if v < u and colors[v] == col:
                    ok = False
                    break
            if not ok:
                continue
            colors[u] = col
            dfs(u + 1)
            colors[u] = None

    dfs(0)
    print(count)

if __name__ == '__main__':
    main()
