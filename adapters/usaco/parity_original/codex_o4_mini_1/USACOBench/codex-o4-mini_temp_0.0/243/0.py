#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    # Grid with padding: indices 0..101, actual field 1..100
    grid = [[False] * 102 for _ in range(102)]
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        grid[x][y] = True

    # BFS to mark outside empty cells
    visited = [[False] * 102 for _ in range(102)]
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102:
                if not visited[nx][ny] and not grid[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny))

    # Compute perimeter: count bale edges adjacent to outside
    perimeter = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if grid[x][y]:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if visited[nx][ny]:
                        perimeter += 1

    print(perimeter)

if __name__ == '__main__':
    main()
