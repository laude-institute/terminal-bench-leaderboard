#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = [[int(c) for c in list(next(it).strip())] for _ in range(n)]
    # Determine bounding rectangles for each color
    bounds = {}
    for i in range(n):
        for j in range(n):
            c = grid[i][j]
            if c == 0:
                continue
            if c not in bounds:
                bounds[c] = [i, i, j, j]
            else:
                bounds[c][0] = min(bounds[c][0], i)
                bounds[c][1] = max(bounds[c][1], i)
                bounds[c][2] = min(bounds[c][2], j)
                bounds[c][3] = max(bounds[c][3], j)
    # Build dependency graph: c -> d if d appears in c's rectangle
    indegree = {c: 0 for c in bounds}
    seen_edge = set()
    for c, (r1, r2, c1, c2) in bounds.items():
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                d = grid[i][j]
                if d != c and d != 0:
                    if (c, d) not in seen_edge:
                        seen_edge.add((c, d))
                        indegree[d] = indegree.get(d, 0) + 1
    # Count colors with zero indegree
    result = sum(1 for c in indegree if indegree[c] == 0)
    print(result)

if __name__ == '__main__':
    main()
