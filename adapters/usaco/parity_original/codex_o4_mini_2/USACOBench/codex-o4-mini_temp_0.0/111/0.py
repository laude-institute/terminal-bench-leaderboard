#!/usr/bin/env python3
"""
Solution to USACO "Bovine Alliance" problem.
Count assignments of M undirected trails among N farms to builders
such that each farm builds at most one trail (out-degree ≤1).
Approach: union-find to find components, track node and edge counts.
For each component:
  if edges > nodes: impossible → 0
  if edges == nodes: one cycle → 2 ways
  if edges < nodes: tree → nodes ways
Multiply results modulo 1e9+7.
"""
import sys

def main():
    sys.setrecursionlimit(10**7)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    parent = list(range(n+1))
    size = [1] * (n+1)
    edges = [0] * (n+1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            edges[ra] += 1
        else:
            # merge smaller into larger
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            edges[ra] += edges[rb] + 1

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        union(u, v)

    MOD = 10**9 + 7
    res = 1
    seen = set()
    for i in range(1, n+1):
        ri = find(i)
        if ri in seen:
            continue
        seen.add(ri)
        cnt_nodes = size[ri]
        cnt_edges = edges[ri]
        if cnt_edges > cnt_nodes:
            print(0)
            return
        if cnt_edges == cnt_nodes:
            res = (res * 2) % MOD
        else:
            # tree component
            res = (res * cnt_nodes) % MOD
    print(res)

if __name__ == '__main__':
    main()
