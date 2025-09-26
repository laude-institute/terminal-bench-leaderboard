#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**7)
mod = 10**9 + 7

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

def count_spanning_trees(num_nodes, edges):
    # Kirchhoff's theorem via Laplacian minor
    if num_nodes <= 1:
        return 1
    # build Laplacian
    L = [[0]*num_nodes for _ in range(num_nodes)]
    for u, v in edges:
        L[u][u] += 1
        L[v][v] += 1
        L[u][v] -= 1
        L[v][u] -= 1
    # build minor by removing last row and col
    m = num_nodes - 1
    M = [[L[i][j] % mod for j in range(m)] for i in range(m)]
    # determinant mod
    det = 1
    for i in range(m):
        # pivot
        pivot = i
        while pivot < m and M[pivot][i] == 0:
            pivot += 1
        if pivot == m:
            return 0
        if pivot != i:
            M[i], M[pivot] = M[pivot], M[i]
            det = (-det) % mod
        inv = pow(M[i][i], mod-2, mod)
        det = det * M[i][i] % mod
        # eliminate
        for j in range(i+1, m):
            if M[j][i] != 0:
                factor = M[j][i] * inv % mod
                for k in range(i, m):
                    M[j][k] = (M[j][k] - factor * M[i][k]) % mod
    return det

def main():
    data = sys.stdin
    n, m = map(int, data.readline().split())
    edges = []
    for _ in range(m):
        a, b, w = map(int, data.readline().split())
        edges.append((w, a-1, b-1))
    edges.sort(key=lambda x: x[0])
    dsu = DSU(n)
    total_weight = 0
    total_count = 1
    i = 0
    while i < m:
        w = edges[i][0]
        # collect same-weight edges
        j = i
        group = []
        while j < m and edges[j][0] == w:
            group.append(edges[j])
            j += 1
        # filter useful edges
        useful = []
        roots = set()
        for _, u, v in group:
            ru = dsu.find(u)
            rv = dsu.find(v)
            if ru != rv:
                useful.append((ru, rv))
                roots.add(ru)
                roots.add(rv)
        if useful:
            # map roots to indices
            root_list = list(roots)
            idx_map = {r:i for i, r in enumerate(root_list)}
            size = len(root_list)
            # build adjacency for comps
            adj = [[] for _ in range(size)]
            for u, v in useful:
                iu = idx_map[u]
                iv = idx_map[v]
                adj[iu].append(iv)
                adj[iv].append(iu)
            visited = [False]*size
            # find components
            for s in range(size):
                if not visited[s]:
                    stack = [s]
                    comp = []
                    visited[s] = True
                    while stack:
                        x = stack.pop()
                        comp.append(x)
                        for y in adj[x]:
                            if not visited[y]:
                                visited[y] = True
                                stack.append(y)
                    t = len(comp)
                    # collect edges in this comp
                    comp_set = set(comp)
                    comp_edges = []
                    for u, v in useful:
                        iu = idx_map[u]
                        iv = idx_map[v]
                        if iu in comp_set and iv in comp_set:
                            comp_edges.append((comp.index(iu), comp.index(iv)))
                    # count trees
                    ct = count_spanning_trees(t, comp_edges)
                    total_count = total_count * ct % mod
            # perform unions and accumulate weight
            for u, v in useful:
                if dsu.union(u, v):
                    total_weight += w
        i = j
    print(f"{total_weight} {total_count}")

if __name__ == '__main__':
    main()
