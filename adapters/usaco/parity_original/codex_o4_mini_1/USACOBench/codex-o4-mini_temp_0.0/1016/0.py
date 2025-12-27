#!/usr/bin/env python3
"""
Solution to the Clock Tree problem.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    # initial clock values for each room
    a = [int(next(it)) for _ in range(N)]
    # build adjacency list
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # bipartite coloring of the tree
    from collections import deque
    color = [-1] * N
    dq = deque([0])
    color[0] = 0
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                dq.append(v)

    # compute required increments for each clock to reach 12
    b = [(12 - ai) % 12 for ai in a]
    # sum over each color class
    s0 = sum(b[i] for i in range(N) if color[i] == 0)
    s1 = sum(b[i] for i in range(N) if color[i] == 1)
    delta = (s0 - s1) % 12

    # determine valid starting rooms
    if delta == 0:
        ans = N
    elif delta == 1:
        # start in color-1 nodes
        ans = sum(1 for i in range(N) if color[i] == 1)
    elif delta == 11:
        # start in color-0 nodes
        ans = sum(1 for i in range(N) if color[i] == 0)
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
