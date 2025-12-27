#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    # Read N, M
    line = input().split()
    if not line:
        return
    n, m = map(int, line)
    # DSU initialization
    parent = list(range(n))
    size = [1] * n
    edges = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        # merge a into b
        parent[a] = b
        size[b] += size[a]
        edges[b] += edges[a]

    # Process edges
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        ru = find(u)
        rv = find(v)
        if ru != rv:
            # union by size
            if size[ru] < size[rv]: ru, rv = rv, ru
            # ru is larger
            union(rv, ru)
            # count this edge
            edges[ru] += 1
        else:
            # internal edge
            edges[ru] += 1

    # Calculate result
    result = 1
    for i in range(n):
        if find(i) == i:
            cnt_nodes = size[i]
            cnt_edges = edges[i]
            if cnt_edges > cnt_nodes:
                print(0)
                return
            if cnt_edges == cnt_nodes - 1:
                # tree component: multiply by number of nodes
                result = result * cnt_nodes % MOD
            elif cnt_edges == cnt_nodes:
                # unicyclic: two orientations
                result = result * 2 % MOD
            # isolated nodes or other cases multiply by 1
    print(result)

if __name__ == "__main__":
    main()
