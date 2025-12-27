#!/usr/bin/env python3
"""
Solve the Cow Steeplechase problem.
Compute maximum number of non-intersecting axis-aligned segments.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    horizontals = []  # list of (x1, x2, y)
    verticals = []    # list of (x, y1, y2)
    for _ in range(n):
        x1 = int(next(it)); y1 = int(next(it))
        x2 = int(next(it)); y2 = int(next(it))
        if y1 == y2:
            # horizontal segment
            x_start, x_end = sorted((x1, x2))
            horizontals.append((x_start, x_end, y1))
        else:
            # vertical segment
            y_start, y_end = sorted((y1, y2))
            verticals.append((x1, y_start, y_end))

    h = len(horizontals)
    v = len(verticals)
    # Build bipartite graph: edges from horizontals to verticals if they intersect
    adj = [[] for _ in range(h)]
    for i, (x1, x2, y) in enumerate(horizontals):
        for j, (x, y1, y2) in enumerate(verticals):
            if x1 <= x <= x2 and y1 <= y <= y2:
                adj[i].append(j)

    # Bipartite matching (Hungarian)
    match_v = [-1] * v

    def dfs(u, seen):
        for w in adj[u]:
            if seen[w]:
                continue
            seen[w] = True
            if match_v[w] == -1 or dfs(match_v[w], seen):
                match_v[w] = u
                return True
        return False

    match_size = 0
    for u in range(h):
        seen = [False] * v
        if dfs(u, seen):
            match_size += 1

    # Maximum independent set in bipartite = total nodes - max matching
    result = n - match_size
    print(result)

if __name__ == '__main__':
    main()
