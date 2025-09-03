#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    # Read edges and sort by relevance descending
    edges = []
    for _ in range(N - 1):
        u, v, r = map(int, input().split())
        # zero-index nodes
        edges.append((r, u - 1, v - 1))
    edges.sort(reverse=True)

    # Read queries and sort by threshold descending
    queries = []
    for i in range(Q):
        k, v = map(int, input().split())
        queries.append((k, v - 1, i))
    queries.sort(reverse=True, key=lambda x: x[0])

    # Disjoint Set Union (union by size)
    parent = list(range(N))
    size = [1] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        # attach smaller to larger
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # Process queries
    ans = [0] * Q
    e = 0
    for k, v, qi in queries:
        # add all edges with relevance >= k
        while e < len(edges) and edges[e][0] >= k:
            _, u, w = edges[e]
            union(u, w)
            e += 1
        # number of other videos in component
        ans[qi] = size[find(v)] - 1

    # Output answers in original order
    out = sys.stdout.write
    for x in ans:
        out(str(x) + '\n')

if __name__ == '__main__':
    main()
