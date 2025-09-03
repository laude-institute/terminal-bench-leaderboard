#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    edges = []
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((w, u-1, v-1))
    queries = []
    for i in range(Q):
        k, v = map(int, input().split())
        queries.append((k, v-1, i))

    # Sort edges by descending weight
    edges.sort(reverse=True)
    # Sort queries by descending k
    queries.sort(reverse=True, key=lambda x: x[0])

    # DSU with size
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
        # union by size
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    res = [0] * Q
    ei = 0
    # Process each query
    for k, v, qi in queries:
        # Add all edges with w >= k
        while ei < len(edges) and edges[ei][0] >= k:
            _, u, wv = edges[ei]
            union(u, wv)
            ei += 1
        # Answer is size of component minus one
        rv = find(v)
        res[qi] = size[rv] - 1

    # Output results in original order
    out = sys.stdout
    for ans in res:
        out.write(str(ans) + '\n')

if __name__ == '__main__':
    main()
