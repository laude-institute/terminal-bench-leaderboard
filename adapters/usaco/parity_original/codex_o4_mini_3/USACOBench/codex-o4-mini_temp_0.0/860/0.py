#!/usr/bin/env python3
"""
Mooyo Mooyo: remove connected regions of size >= K and apply gravity until stable.
"""
import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

    # Repeat removal and gravity until no more regions to remove
    while True:
        removed_any = False
        visited = [[False] * 10 for _ in range(N)]
        to_remove = [[False] * 10 for _ in range(N)]

        # Find connected regions
        for i in range(N):
            for j in range(10):
                if grid[i][j] != '0' and not visited[i][j]:
                    color = grid[i][j]
                    stack = [(i, j)]
                    region = [(i, j)]
                    visited[i][j] = True
                    # DFS to collect region
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < 10:
                                if not visited[nx][ny] and grid[nx][ny] == color:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny))
                                    region.append((nx, ny))
                    # Mark for removal if large enough
                    if len(region) >= K:
                        removed_any = True
                        for x, y in region:
                            to_remove[x][y] = True

        # Stop if no removals
        if not removed_any:
            break

        # Remove marked cells
        for i in range(N):
            for j in range(10):
                if to_remove[i][j]:
                    grid[i][j] = '0'

        # Apply gravity per column
        for j in range(10):
            write_row = N - 1
            for i in range(N - 1, -1, -1):
                if grid[i][j] != '0':
                    grid[write_row][j] = grid[i][j]
                    if write_row != i:
                        grid[i][j] = '0'
                    write_row -= 1

    # Output final grid
    for row in grid:
        sys.stdout.write(''.join(row) + '\n')

if __name__ == '__main__':
    main()
