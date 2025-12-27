#!/usr/bin/env python3
"""
USACO Bronze "pageant" problem:
Given an N x M grid with exactly two connected spots marked 'X',
find the minimum number of '.' cells to paint 'X' to connect them.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    grid = [list(next(it).strip()) for _ in range(n)]

    # DFS to find connected components of 'X'
    visited = [[False]*m for _ in range(n)]
    components = []

    def dfs(r, c, comp):
        stack = [(r, c)]
        visited[r][c] = True
        while stack:
            x, y = stack.pop()
            comp.append((x, y))
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 'X':
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X' and not visited[i][j]:
                comp = []
                dfs(i, j, comp)
                components.append(comp)
                if len(components) == 2:
                    break
        if len(components) == 2:
            break

    comp1, comp2 = components
    # Compute minimum painting distance
    best = float('inf')
    for x1, y1 in comp1:
        for x2, y2 in comp2:
            # Manhattan distance minus 1
            dist = abs(x1 - x2) + abs(y1 - y2) - 1
            if dist < best:
                best = dist

    print(best)

if __name__ == '__main__':
    main()
