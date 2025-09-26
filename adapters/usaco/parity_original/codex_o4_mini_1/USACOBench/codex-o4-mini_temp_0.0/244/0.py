#!/usr/bin/env python3
"""
Compute the perimeter of connected hay bales region excluding holes.
"""
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N = int(input())
    bales = set()
    min_x = 10**7
    max_x = 0
    min_y = 10**7
    max_y = 0
    # Read bale positions and track bounds
    for _ in range(N):
        x, y = map(int, input().split())
        bales.add((x, y))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # Define flood-fill bounds around the shape
    xmin = min_x - 1
    xmax = max_x + 1
    ymin = min_y - 1
    ymax = max_y + 1

    # Start BFS from an exterior empty cell
    start = (xmin, ymin)
    visited = {start}
    queue = deque([start])
    perimeter = 0
    # Four cardinal directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Flood fill empty space and count adjacent bale edges
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Skip out-of-bounds
            if nx < xmin or nx > xmax or ny < ymin or ny > ymax:
                continue
            if (nx, ny) in bales:
                perimeter += 1
            elif (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    # Output the computed perimeter
    print(perimeter)

if __name__ == '__main__':
    main()
