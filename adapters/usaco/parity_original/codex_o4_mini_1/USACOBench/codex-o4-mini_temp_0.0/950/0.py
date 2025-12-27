#!/usr/bin/env python3
import sys
sys.setrecursionlimit(1000000)
def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    grid = [list(map(int, [next(it) for _ in range(n)])) for _ in range(n)]
    # prepare list of cells with heights
    cells = []  # (h, i, j)
    for i in range(n):
        for j in range(n):
            cells.append((grid[i][j], i, j))
    # sort ascending and descending
    asc = sorted(cells)
    desc = list(reversed(asc))
    # Disjoint set for >h graph (complement connectivity)
    N = n * n
    parent_out = list(range(N + 1))  # extra node for outside
    size_out = [1] * (N + 1)
    added_out = [False] * N
    outside = N
    def find_out(x):
        while parent_out[x] != x:
            parent_out[x] = parent_out[parent_out[x]]
            x = parent_out[x]
        return x
    def union_out(a, b):
        ra = find_out(a); rb = find_out(b)
        if ra == rb: return
        if size_out[ra] < size_out[rb]: ra, rb = rb, ra
        parent_out[rb] = ra
        size_out[ra] += size_out[rb]
    # record if >h graph is connected at each threshold
    conn = {}
    cnt_out = 0
    # 8 directions for pointwise
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for h, i, j in desc:
        # before adding this cell, >h includes cnt_out cells
        root_out = find_out(outside)
        # if outside component size == cnt_out + 1 => all >h connect to outside
        conn[h] = (size_out[root_out] == cnt_out + 1)
        # add this cell to >h graph
        idx = i * n + j
        added_out[idx] = True
        cnt_out += 1
        # connect to outside if on border
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            union_out(idx, outside)
        # union with >h neighbors
        for di, dj in dirs8:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                nid = ni * n + nj
                if added_out[nid]:
                    union_out(idx, nid)
    # Disjoint set for <=h graph (region connectivity)
    parent_in = list(range(N))
    size_in = [1] * N
    added_in = [False] * N
    def find_in(x):
        while parent_in[x] != x:
            parent_in[x] = parent_in[parent_in[x]]
            x = parent_in[x]
        return x
    def union_in(a, b):
        ra = find_in(a); rb = find_in(b)
        if ra == rb: return
        if size_in[ra] < size_in[rb]: ra, rb = rb, ra
        parent_in[rb] = ra
        size_in[ra] += size_in[rb]
    # 4 directions for edgewise
    dirs4 = [(-1,0),(1,0),(0,-1),(0,1)]
    ans = 0
    # build regions and sum sizes of valleys
    for h, i, j in asc:
        idx = i * n + j
        added_in[idx] = True
        # union with <=h neighbors
        for di, dj in dirs4:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                nid = ni * n + nj
                if added_in[nid]:
                    union_in(idx, nid)
        # if complement >h is connected, this region is non-holey valley
        if conn.get(h, True):
            root = find_in(idx)
            ans += size_in[root]
    print(ans)

if __name__ == '__main__':
    main()
