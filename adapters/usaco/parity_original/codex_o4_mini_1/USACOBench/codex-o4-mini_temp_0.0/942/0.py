#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # read grid and map R->1, L->0
    grid = [list(next(it).strip()) for _ in range(n)]
    g = [[1 if grid[i][j] == 'R' else 0 for j in range(n)] for i in range(n)]
    # compute error matrix E for i>0, j>0
    # E[i][j] = g[i][j] ^ g[i][0] ^ g[0][j] ^ g[0][0]
    tot = 0
    # row and col violations counts (for i>0,j>0)
    rowV = [0] * n
    colV = [0] * n
    # store one position if tot==1
    single = None
    for i in range(1, n):
        for j in range(1, n):
            if (g[i][j] ^ g[i][0] ^ g[0][j] ^ g[0][0]) == 1:
                tot += 1
                rowV[i] += 1
                colV[j] += 1
                single = (i, j) if single is None else single
    candidates = []
    # case A: single violation
    if tot == 1 and single is not None:
        candidates.append(single)
    # case C/D: a full row or full col in submatrix
    if tot == n - 1:
        # row case: row i has all errors
        for i in range(1, n):
            if rowV[i] == n - 1:
                candidates.append((i, 0))
                break
        # col case: col j has all errors
        for j in range(1, n):
            if colV[j] == n - 1:
                candidates.append((0, j))
                break
    # case B: full submatrix
    if tot == (n - 1) * (n - 1):
        candidates.append((0, 0))
    # select smallest candidate
    if not candidates:
        print(-1)
    else:
        # sort by row, then col
        p, q = min(candidates)
        # convert to 1-based
        print(p + 1, q + 1)

if __name__ == '__main__':
    main()
