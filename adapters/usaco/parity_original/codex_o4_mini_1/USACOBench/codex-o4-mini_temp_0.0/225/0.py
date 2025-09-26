#!/usr/bin/env python3
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.parity = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            px = self.parent[x]
            root, par = self.find(px)
            self.parity[x] ^= par
            self.parent[x] = root
        return self.parent[x], self.parity[x]

    def union(self, x, y, val):
        rx, px = self.find(x)
        ry, py = self.find(y)
        if rx == ry:
            return (px ^ py) == val
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            px, py = py, px
        self.parent[ry] = rx
        self.parity[ry] = px ^ py ^ val
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    uf = UnionFind(n)
    ans = m
    idx = 2
    for i in range(1, m + 1):
        x = int(data[idx]) - 1
        y = int(data[idx+1]) - 1
        t = data[idx+2]
        idx += 3
        val = 0 if t == 'T' else 1
        if not uf.union(x, y, val):
            ans = i - 1
            break
    print(ans)

if __name__ == '__main__':
    main()
