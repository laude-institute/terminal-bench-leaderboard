#!/usr/bin/env python3
import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(N)]
    dsu = DSU(N)
    for _ in range(M):
        a, b = map(int, input().split())
        dsu.union(a-1, b-1)

    # Initialize bounding boxes
    INF = 10**18
    minx = [INF] * N
    maxx = [-INF] * N
    miny = [INF] * N
    maxy = [-INF] * N

    # Compute bounds for each component
    for i, (x, y) in enumerate(coords):
        r = dsu.find(i)
        if x < minx[r]: minx[r] = x
        if x > maxx[r]: maxx[r] = x
        if y < miny[r]: miny[r] = y
        if y > maxy[r]: maxy[r] = y

    # Find smallest perimeter
    ans = INF
    for i in range(N):
        if dsu.find(i) == i:
            perim = 2 * (maxx[i] - minx[i]) + 2 * (maxy[i] - miny[i])
            if perim < ans:
                ans = perim
    print(ans)

if __name__ == '__main__':
    main()
