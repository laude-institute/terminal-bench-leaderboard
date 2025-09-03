#!/usr/bin/env python3
"""
Compute the perimeter of a connected region of hay bales,
ignoring holes.
Approach: flood-fill from outside the bounding box to count external edges.
"""
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N = int(input())
    coords = []
    min_x = 10**9
    min_y = 10**9
    max_x = 0
    max_y = 0
    for _ in range(N):
        x, y = map(int, input().split())
        coords.append((x, y))
        if x < min_x: min_x = x
        if y < min_y: min_y = y
        if x > max_x: max_x = x
        if y > max_y: max_y = y

    # extend bounding box by 1 in all directions
    shift_x = min_x - 1
    shift_y = min_y - 1
    width = max_x - min_x + 3
    height = max_y - min_y + 3

    # build grid: 0 empty, 1 bale
    grid = [[0] * width for _ in range(height)]
    for x, y in coords:
        grid[y - shift_y][x - shift_x] = 1

    # flood-fill empty space from (0,0)
    visited = [[False] * width for _ in range(height)]
    dq = deque()
    dq.append((0, 0))
    visited[0][0] = True
    perimeter = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while dq:
        cx, cy = dq.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if grid[ny][nx] == 1:
                perimeter += 1
            elif not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((nx, ny))

    print(perimeter)

if __name__ == '__main__':
    main()
