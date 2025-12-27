#!/usr/bin/env python3
"""
Pseudocode:
1. Read N (number of videos) and Q (number of queries)
2. Read N-1 edges: each with videos p, q and relevance r
3. Read Q queries: each with threshold k and video v, store original index
4. Sort edges in descending order by relevance r
5. Sort queries in descending order by k
6. Initialize DSU structure for N videos with parent[i]=i and size[i]=1
7. Initialize answers array of length Q
8. Set edge_ptr = 0
9. For each query (k, v, idx) in sorted queries:
     a. While edge_ptr < len(edges) and edges[edge_ptr].r >= k:
         i.   Union the two videos of this edge in DSU
         ii.  Increment edge_ptr
     b. Set answers[idx] = DSU.size[DSU.find(v)] - 1  # exclude v itself
10. Output answers in original order, one per line
"""

import sys

class DSU:
    def __init__(self, n):
        # 1-based indexing: videos 1..n
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        # attach smaller root to larger root
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    edges = []
    for _ in range(n-1):
        p = int(next(it))
        qq = int(next(it))
        r = int(next(it))
        edges.append((r, p, qq))
    queries = []
    for i in range(q):
        k = int(next(it))
        v = int(next(it))
        queries.append((k, v, i))
    # sort edges and queries
    edges.sort(key=lambda x: x[0], reverse=True)
    queries.sort(key=lambda x: x[0], reverse=True)
    dsu = DSU(n)
    answers = [0] * q
    edge_ptr = 0
    # process queries
    for k, v, idx in queries:
        while edge_ptr < len(edges) and edges[edge_ptr][0] >= k:
            _, u, w = edges[edge_ptr]
            dsu.union(u, w)
            edge_ptr += 1
        # count videos reachable from v with relevance >= k
        root = dsu.find(v)
        answers[idx] = dsu.size[root] - 1
    # output answers
    out = sys.stdout
    for ans in answers:
        out.write(str(ans) + '\n')

if __name__ == '__main__':
    main()
