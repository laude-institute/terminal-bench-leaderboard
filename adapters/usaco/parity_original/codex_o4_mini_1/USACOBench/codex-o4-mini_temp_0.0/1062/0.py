#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    edges = list(map(int, data[1:]))
    adj = [[] for _ in range(n+1)]
    for i in range(0, len(edges), 2):
        a, b = edges[i], edges[i+1]
        adj[a].append(b)
        adj[b].append(a)

    # BFS to build tree and count children
    parent = [0] * (n+1)
    children_count = [0] * (n+1)
    q = deque([1])
    parent[1] = -1
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                children_count[u] += 1
                q.append(v)

    # Compute doubling days: sum of ceil(log2(children+1))
    doubling_days = 0
    for u in range(1, n+1):
        c = children_count[u]
        # ceil(log2(c+1)) == bit_length of c
        if c > 0:
            doubling_days += c.bit_length()

    # Movement days = n-1 edges to traverse
    movement_days = n - 1
    print(doubling_days + movement_days)

if __name__ == '__main__':
    main()
