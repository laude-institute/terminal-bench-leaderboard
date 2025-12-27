#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    grid = [list(next(it).strip()) for _ in range(n)]
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]
    ans = 0
    # try mapping encrypted letter cM -> 'M', cO -> 'O'
    from string import ascii_uppercase as UC
    for cM in UC:
        if cM == 'M':
            continue
        for cO in UC:
            if cO == 'O' or cO == cM:
                continue
            cnt = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] != cM:
                        continue
                    # check each direction for 'O','O'
                    for dx, dy in dirs:
                        x1, y1 = i + dx, j + dy
                        x2, y2 = x1 + dx, y1 + dy
                        if 0 <= x2 < n and 0 <= y2 < m:
                            if grid[x1][y1] == cO and grid[x2][y2] == cO:
                                cnt += 1
            if cnt > ans:
                ans = cnt
    print(ans)

if __name__ == '__main__':
    main()
