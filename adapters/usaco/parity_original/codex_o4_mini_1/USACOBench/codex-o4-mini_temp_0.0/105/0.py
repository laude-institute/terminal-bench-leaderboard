#!/usr/bin/env python3
"""
USACO 2012 Grazing Patterns

Each half-hour, Bessie starts at (1,1) and Mildred at (5,5) on a 5x5 grid
with some barren squares. They simultaneously move to adjacent grassy squares,
eat grass, cover all grassy squares, and end at the same final square.
Count the number of valid movement sequences without collisions until the end.
"""
import sys

def main():
    sys.setrecursionlimit(10**7)
    data = sys.stdin.read().split()
    # Parse input
    K = int(data[0])
    grid = [[True] * 5 for _ in range(5)]
    idx = 1
    for _ in range(K):
        i = int(data[idx]) - 1; j = int(data[idx+1]) - 1
        idx += 2
        grid[i][j] = False
    # Count total grassy squares
    total_grass = sum(grid[r][c] for r in range(5) for c in range(5))
    # Visited map: mark barren as visited to skip
    visited = [[False] * 5 for _ in range(5)]
    # Start positions (0,0) and (4,4)
    visited[0][0] = True
    visited[4][4] = True
    # Directions: N, S, E, W
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # Counter for valid ways
    count = 0

    def dfs(ax, ay, bx, by, visited_count):
        nonlocal count
        # All grass eaten
        if visited_count == total_grass:
            if ax == bx and ay == by:
                count += 1
            return
        # One square left: must meet there
        if visited_count == total_grass - 1:
            for dx, dy in dirs:
                nax, nay = ax + dx, ay + dy
                if not (0 <= nax < 5 and 0 <= nay < 5):
                    continue
                if not grid[nax][nay] or visited[nax][nay]:
                    continue
                # Check if Mildred can also move there
                for dx2, dy2 in dirs:
                    nbx, nby = bx + dx2, by + dy2
                    if nbx == nax and nby == nay:
                        if 0 <= nbx < 5 and 0 <= nby < 5 and grid[nbx][nby] and not visited[nbx][nby]:
                            count += 1
                # No further branching
            return

        # Regular moves: both move to distinct unvisited grassy squares
        for dx, dy in dirs:
            nax, nay = ax + dx, ay + dy
            if not (0 <= nax < 5 and 0 <= nay < 5):
                continue
            if not grid[nax][nay] or visited[nax][nay]:
                continue
            visited[nax][nay] = True
            for dx2, dy2 in dirs:
                nbx, nby = bx + dx2, by + dy2
                if not (0 <= nbx < 5 and 0 <= nby < 5):
                    continue
                if not grid[nbx][nby] or visited[nbx][nby]:
                    continue
                # Prevent premature collision
                if nax == nbx and nay == nby:
                    continue
                visited[nbx][nby] = True
                dfs(nax, nay, nbx, nby, visited_count + 2)
                visited[nbx][nby] = False
            visited[nax][nay] = False

    # Start DFS with both starting at opposite corners and 2 eaten squares
    dfs(0, 0, 4, 4, 2)
    # Output result
    print(count)

if __name__ == '__main__':
    main()
