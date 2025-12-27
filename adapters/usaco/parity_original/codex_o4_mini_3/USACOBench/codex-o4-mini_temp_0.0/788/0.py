#!/usr/bin/env python3
"""
Solution for MooTube relevance queries.
Uses DSU to answer for each query how many videos have relevance >= K.
"""
import sys

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    # Read edges: (relevance, u, v)
    edges = []
    for _ in range(N - 1):
        u, v, r = map(int, input().split())
        # zero-index nodes
        edges.append((r, u - 1, v - 1))
    # Read queries: (K, node, original_index)
    queries = []
    for i in range(Q):
        k, v = map(int, input().split())
        queries.append((k, v - 1, i))

    # Sort edges descending by relevance
    edges.sort(key=lambda x: x[0], reverse=True)
    # Sort queries descending by K
    queries.sort(key=lambda x: x[0], reverse=True)

    # DSU structures
    parent = list(range(N))
    size = [1] * N

    def find(x):
        # path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        # union by size
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # Answer queries
    res = [0] * Q
    e_idx = 0
    for k, v, qi in queries:
        # include all edges with relevance >= k
        while e_idx < len(edges) and edges[e_idx][0] >= k:
            _, u, w = edges[e_idx]
            union(u, w)
            e_idx += 1
        # subtract one to exclude the video itself
        res[qi] = size[find(v)] - 1

    # Output results in original order
    print("\n".join(map(str, res)))


if __name__ == '__main__':
    main()
