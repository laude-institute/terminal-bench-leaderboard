#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    # Read edges: (relevance, u, v)
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    # Read queries: (threshold k, node v, original index)
    queries = []
    for idx in range(Q):
        k, v = map(int, input().split())
        queries.append((k, v, idx))
    # Sort edges and queries descending by relevance/threshold
    edges.sort(reverse=True, key=lambda x: x[0])
    queries.sort(reverse=True, key=lambda x: x[0])
    # DSU setup
    parent = list(range(N + 1))
    size = [1] * (N + 1)

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
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    # Process queries
    ans = [0] * Q
    ei = 0
    for k, v, idx in queries:
        # Add all edges with relevance >= k
        while ei < len(edges) and edges[ei][0] >= k:
            _, u, wv = edges[ei]
            union(u, wv)
            ei += 1
        # Number of videos reachable from v with min relevance >= k
        ans[idx] = size[find(v)] - 1

    # Output answers
    print("\n".join(map(str, ans)))

if __name__ == '__main__':
    main()
