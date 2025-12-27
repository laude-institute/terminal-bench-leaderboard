#!/usr/bin/env python3
import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        # parity[i]: parity from i to its parent (0 = same, 1 = opposite)
        self.parity = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            px = self.parent[x]
            root, par = self.find(px)
            self.parity[x] ^= par
            self.parent[x] = root
        return self.parent[x], self.parity[x]

    def union(self, x, y, p):
        # enforce that parity between x and y is p (0 equal, 1 opposite)
        rx, px = self.find(x)
        ry, py = self.find(y)
        if rx == ry:
            return (px ^ py) == p
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            px, py = py, px
        self.parent[ry] = rx
        # set parity so that px ^ parity_link ^ py == p
        self.parity[ry] = px ^ py ^ p
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    statements = []
    idx = 2
    for _ in range(M):
        x = int(data[idx]); y = int(data[idx+1]); c = data[idx+2]
        statements.append((x-1, y-1, c))
        idx += 3

    def check(k):
        dsu = DSU(N)
        for i in range(k):
            x, y, c = statements[i]
            p = 1 if c == 'L' else 0
            if not dsu.union(x, y, p):
                return False
        return True

    # binary search largest prefix
    lo, hi = 0, M
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == '__main__':
    main()
