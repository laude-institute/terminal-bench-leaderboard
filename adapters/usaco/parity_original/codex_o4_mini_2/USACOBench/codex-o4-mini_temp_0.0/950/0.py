#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    # Prepare cells sorted by height
    cells = []  # list of (height, i, j)
    for i in range(N):
        for j in range(N):
            cells.append((H[i][j], i, j))
    cells.sort()

    # DSU structures
    parent = [-1] * (N * N)
    size = [0] * (N * N)
    is_holey = [False] * (N * N)
    active = [[False] * N for _ in range(N)]

    def find(x):
        # path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return ra
        # union by size
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        is_holey[ra] = is_holey[ra] or is_holey[rb]
        return ra

    # Neighbor directions
    dirs4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dirs8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    ans = 0
    # Process cells in increasing height
    for h, i, j in cells:
        idx = i * N + j
        # activate this cell
        parent[idx] = idx
        size[idx] = 1
        is_holey[idx] = False
        active[i][j] = True

        # merge with active 4-neighbors
        for di, dj in dirs4:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and active[ni][nj]:
                idx2 = ni * N + nj
                idx = union(idx, idx2)

        root = find(idx)

        # check for new holes created around this activation
        for di, dj in dirs8:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not active[ni][nj]:
                # if all 8 neighbors of (ni,nj) are active, it's a hole cell
                hole = True
                for ddi, ddj in dirs8:
                    xi, xj = ni + ddi, nj + ddj
                    if not (0 <= xi < N and 0 <= xj < N and active[xi][xj]):
                        hole = False
                        break
                if hole:
                    is_holey[root] = True

        # if this region is not holey, add its size
        if not is_holey[root]:
            ans += size[root]

    print(ans)


if __name__ == '__main__':
    main()
