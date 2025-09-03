#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    horizontals = []  # (x1, x2, y)
    verticals = []    # (x, y1, y2)
    for _ in range(N):
        x1 = int(next(it)); y1 = int(next(it))
        x2 = int(next(it)); y2 = int(next(it))
        if y1 == y2:
            # horizontal segment
            a, b = sorted((x1, x2))
            horizontals.append((a, b, y1))
        else:
            # vertical segment
            c = x1
            a, b = sorted((y1, y2))
            verticals.append((c, a, b))
    H = len(horizontals)
    V = len(verticals)
    # build bipartite graph: horizontal -> list of verticals it intersects
    adj = [[] for _ in range(H)]
    for i, (x1, x2, y) in enumerate(horizontals):
        for j, (x, y1, y2) in enumerate(verticals):
            if x1 <= x <= x2 and y1 <= y <= y2:
                adj[i].append(j)

    # bipartite matching from horizontals (U) to verticals (V)
    match = [-1] * V

    def dfs(u, seen):
        for v in adj[u]:
            if seen[v]:
                continue
            seen[v] = True
            if match[v] == -1 or dfs(match[v], seen):
                match[v] = u
                return True
        return False

    msize = 0
    for u in range(H):
        seen = [False] * V
        if dfs(u, seen):
            msize += 1

    # max independent set size = N - max matching size
    print(N - msize)


if __name__ == '__main__':
    main()
