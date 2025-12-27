#!/usr/bin/env python3
import collections

def main():
    # Read the 10x10 grid
    grid = [input().strip() for _ in range(10)]

    # Find barn (B) and lake (L) positions
    start = None
    target = None
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'B':
                start = (i, j)
            elif grid[i][j] == 'L':
                target = (i, j)

    # BFS to find shortest path from barn to lake avoiding the rock (R)
    dq = collections.deque()
    dq.append(start)
    visited = [[False]*10 for _ in range(10)]
    visited[start[0]][start[1]] = True
    dist = [[0]*10 for _ in range(10)]

    # Directions: up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while dq:
        x, y = dq.popleft()
        # Stop if we've reached the lake
        if (x, y) == target:
            break
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if not visited[nx][ny] and grid[nx][ny] != 'R':
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))

    # Number of cows is distance minus 1 (exclude B and L themselves)
    result = dist[target[0]][target[1]] - 1
    print(result)

if __name__ == '__main__':
    main()
