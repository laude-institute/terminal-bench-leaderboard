#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    horizontals = []  # tuples of (x1, x2, y)
    verticals = []    # tuples of (x, y1, y2)
    for _ in range(n):
        x1 = int(next(it))
        y1 = int(next(it))
        x2 = int(next(it))
        y2 = int(next(it))
        if y1 == y2:
            # horizontal segment
            xa, xb = sorted((x1, x2))
            horizontals.append((xa, xb, y1))
        else:
            # vertical segment
            ya, yb = sorted((y1, y2))
            verticals.append((x1, ya, yb))

    H = len(horizontals)
    V = len(verticals)
    # build bipartite graph: H nodes on left, V on right
    adj = [[] for _ in range(H)]
    for i, (xa, xb, y) in enumerate(horizontals):
        for j, (x, ya, yb) in enumerate(verticals):
            if xa <= x <= xb and ya <= y <= yb:
                adj[i].append(j)

    # array to record match for vertical nodes
    matchV = [-1] * V

    def dfs(u, seen):
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                if matchV[v] == -1 or dfs(matchV[v], seen):
                    matchV[v] = u
                    return True
        return False

    # find maximum matching
    match = 0
    for u in range(H):
        seen = [False] * V
        if dfs(u, seen):
            match += 1

    # maximum independent set in bipartite graph = total nodes - max matching
    result = n - match
    print(result)

if __name__ == '__main__':
    main()
