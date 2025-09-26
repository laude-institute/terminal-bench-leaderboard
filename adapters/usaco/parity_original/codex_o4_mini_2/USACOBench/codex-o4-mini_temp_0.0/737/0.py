#!/usr/bin/env python3
"""
Solution for counting possible first-painted colors on a canvas.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    grid = [list(map(int, list(data[i+1]))) for i in range(n)]

    # Determine visible colors
    visible = set()
    for row in grid:
        for c in row:
            if c != 0:
                visible.add(c)

    # Initialize bounding boxes for each color
    inf = float('inf')
    bounds = {c: [inf, -inf, inf, -inf] for c in visible}
    # bounds[c] = [min_r, max_r, min_c, max_c]
    for r in range(n):
        for c in range(n):
            col = grid[r][c]
            if col and col in bounds:
                b = bounds[col]
                b[0] = min(b[0], r)
                b[1] = max(b[1], r)
                b[2] = min(b[2], c)
                b[3] = max(b[3], c)

    # Build dependency graph edges: c -> d if d overwrote c
    indegree = {c: 0 for c in visible}
    for c in visible:
        min_r, max_r, min_c, max_c = bounds[c]
        for r in range(min_r, max_r + 1):
            for co in range(min_c, max_c + 1):
                d = grid[r][co]
                if d != c and d != 0:
                    # c must be painted before d
                    # count indegree for d
                    # ensure counting each once per pair
                    # we can mark by changing bounds or use a set
                    # simplest: track seen pairs
                    pass

    # To avoid double-counting, track seen pairs
    seen = set()
    indegree = {c: 0 for c in visible}
    for c in visible:
        min_r, max_r, min_c, max_c = bounds[c]
        for r in range(min_r, max_r + 1):
            for co in range(min_c, max_c + 1):
                d = grid[r][co]
                if d != c and d != 0:
                    if (c, d) not in seen:
                        seen.add((c, d))
                        indegree[d] += 1

    # Count colors with indegree 0 (possible first painted)
    result = sum(1 for c in visible if indegree[c] == 0)
    print(result)

if __name__ == '__main__':
    main()
