#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input())
    # grid with padding: 0..101
    max_coord = 100
    grid = [[False] * (max_coord + 2) for _ in range(max_coord + 2)]
    for _ in range(n):
        x, y = map(int, input().split())
        grid[x][y] = True
    # BFS from (0,0) to mark outside empty cells
    visited = [[False] * (max_coord + 2) for _ in range(max_coord + 2)]
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = True
    # directions: N, S, E, W
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    perimeter = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            # check bounds
            if 0 <= nx <= max_coord + 1 and 0 <= ny <= max_coord + 1:
                if grid[nx][ny]:
                    # adjacent to a bale: contributes to perimeter
                    perimeter += 1
                elif not visited[nx][ny]:
                    # empty and not visited: part of outside
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    # output result
    print(perimeter)

if __name__ == '__main__':
    main()
