#!/usr/bin/env python3
"""
Compute the minimum number of new 'X's needed to connect two spots on a grid.
"""
import sys
from collections import deque

def read_input():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    grid = [list(row) for row in data[2:2+n]]
    return n, m, grid

def find_region(n, m, grid, visited, start_r, start_c):
    """Return list of cells in the connected region starting at (start_r, start_c)."""
    region = []
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = True
    while stack:
        r, c = stack.pop()
        region.append((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 'X':
                visited[nr][nc] = True
                stack.append((nr, nc))
    return region

def main():
    n, m, grid = read_input()
    visited = [[False]*m for _ in range(n)]
    regions = []
    # find the two spots
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X' and not visited[i][j]:
                regions.append(find_region(n, m, grid, visited, i, j))
                if len(regions) == 2:
                    break
        if len(regions) == 2:
            break

    region1, region2 = regions
    # mark region2 cells for quick lookup
    target = set(region2)
    # 0-1 BFS from all cells in region1
    INF = 10**9
    dist = [[INF]*m for _ in range(n)]
    dq = deque()
    for r, c in region1:
        dist[r][c] = 0
        dq.appendleft((r, c))

    while dq:
        r, c = dq.popleft()
        # reached second spot
        if (r, c) in target:
            print(dist[r][c])
            return
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m:
                cost = 0 if grid[nr][nc] == 'X' else 1
                nd = dist[r][c] + cost
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

if __name__ == '__main__':
    main()
