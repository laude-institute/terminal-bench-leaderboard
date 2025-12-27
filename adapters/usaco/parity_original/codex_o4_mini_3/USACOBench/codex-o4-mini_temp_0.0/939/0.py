#!/usr/bin/env python3
import sys
from collections import deque

def main():
    # Read the 10x10 grid
    grid = [list(sys.stdin.readline().strip()) for _ in range(10)]
    start = None
    target = None
    # Locate barn (B) and lake (L)
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'B':
                start = (i, j)
            elif grid[i][j] == 'L':
                target = (i, j)

    # BFS to find shortest path from B to L, avoiding rock (R)
    visited = [[False] * 10 for _ in range(10)]
    q = deque()
    q.append((start[0], start[1], 0))  # (row, col, distance)
    visited[start[0]][start[1]] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, dist = q.popleft()
        # If reached lake, output cows count = path length - 1
        if (x, y) == target:
            print(dist - 1)
            return
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if not visited[nx][ny] and grid[nx][ny] != 'R':
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

if __name__ == '__main__':
    main()
