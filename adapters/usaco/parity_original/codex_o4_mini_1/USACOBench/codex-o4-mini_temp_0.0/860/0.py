#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    # Read grid as list of lists of ints
    grid = [list(map(int, list(input().strip()))) for _ in range(N)]
    # Repeat until no more removals
    while True:
        visited = [[False] * 10 for _ in range(N)]
        to_remove = []
        # Find connected components
        for i in range(N):
            for j in range(10):
                if grid[i][j] != 0 and not visited[i][j]:
                    color = grid[i][j]
                    stack = [(i, j)]
                    comp = [(i, j)]
                    visited[i][j] = True
                    # DFS to collect component
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < 10:
                                if not visited[nx][ny] and grid[nx][ny] == color:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny))
                                    comp.append((nx, ny))
                    # Mark for removal if size >= K
                    if len(comp) >= K:
                        to_remove.extend(comp)
        # If no removals, we're done
        if not to_remove:
            break
        # Remove marked cells
        for x, y in to_remove:
            grid[x][y] = 0
        # Apply gravity column by column
        for col in range(10):
            stack = []
            # Collect non-zero values
            for row in range(N):
                if grid[row][col] != 0:
                    stack.append(grid[row][col])
            # Build new column: zeros on top, values at bottom
            zeros = [0] * (N - len(stack))
            new_col = zeros + stack
            for row in range(N):
                grid[row][col] = new_col[row]
    # Output final grid
    for row in grid:
        print(''.join(map(str, row)))

if __name__ == '__main__':
    main()
