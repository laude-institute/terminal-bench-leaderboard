#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    # Read number of hay bales
    N = int(input())
    # Read bale coordinates
    hay_bales = [tuple(map(int, input().split())) for _ in range(N)]

    # Grid size with padding for boundary flooding (0..101)
    size = 102
    # Mark occupied cells
    occupied = [[False] * size for _ in range(size)]
    for x, y in hay_bales:
        occupied[x][y] = True

    # Flood-fill from outside to mark reachable empty cells
    visited = [[False] * size for _ in range(size)]
    queue = deque()
    # Start from (0,0)
    queue.append((0, 0))
    visited[0][0] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < size and 0 <= ny < size:
                if not visited[nx][ny] and not occupied[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    # Calculate perimeter: edges between bales and outside-reachable empty cells
    perimeter = 0
    for x, y in hay_bales:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny]:
                perimeter += 1

    # Output result
    print(perimeter)

if __name__ == '__main__':
    main()
