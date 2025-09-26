#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Normalize clock values mod 12
    a = [0] + [int(next(it)) % 12 for _ in range(n)]
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    # Bipartition the tree by BFS
    from collections import deque
    color = [None] * (n+1)
    q = deque([1])
    color[1] = 0
    cnt = [0, 0]
    summod = [0, 0]
    while q:
        u = q.popleft()
        c = color[u]
        cnt[c] += 1
        summod[c] = (summod[c] + a[u]) % 12
        for v in adj[u]:
            if color[v] is None:
                color[v] = 1 - c
                q.append(v)
    sa, sb = summod[0], summod[1]
    ca, cb = cnt[0], cnt[1]
    # Determine valid starting rooms count
    if sa == sb:
        res = n
    elif sa == (sb + 1) % 12:
        res = ca
    elif sb == (sa + 1) % 12:
        res = cb
    else:
        res = 0
    print(res)

if __name__ == "__main__":
    main()
