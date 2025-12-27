#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    grid = [list(next(it)) for _ in range(n)]

    # Directions: 8 neighbors
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    letters = [chr(ord('A') + i) for i in range(26)]
    max_count = 0

    for x in letters:
        # x maps to 'M'
        if x == 'M':
            continue
        for y in letters:
            # y maps to 'O'
            if y == 'O' or y == x:
                continue
            count = 0
            # scan all positions and directions
            for i in range(n):
                for j in range(m):
                    if grid[i][j] != x:
                        continue
                    for dx, dy in dirs:
                        i1 = i + dx
                        j1 = j + dy
                        i2 = i + 2*dx
                        j2 = j + 2*dy
                        if 0 <= i1 < n and 0 <= j1 < m and 0 <= i2 < n and 0 <= j2 < m:
                            if grid[i1][j1] == y and grid[i2][j2] == y:
                                count += 1
            if count > max_count:
                max_count = count

    print(max_count)

if __name__ == '__main__':
    main()
