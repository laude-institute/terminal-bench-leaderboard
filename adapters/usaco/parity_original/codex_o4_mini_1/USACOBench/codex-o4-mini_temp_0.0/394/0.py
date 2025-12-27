#!/usr/bin/env python3
import sys
sys.setrecursionlimit(1000000)
def main():
    data = sys.stdin
    N, M = map(int, data.readline().split())
    grid = [data.readline().strip() for _ in range(N)]
    memo = [[[None]*4 for _ in range(M)] for _ in range(N)]
    slash_map = [1,0,3,2]
    back_map  = [1,2,3,0]
    delta = [(-1,0),(0,1),(1,0),(0,-1)]
    def compute(i, j, dir):
        path = []
        visited = {}
        ci, cj, cdir = i, j, dir
        while True:
            if ci < 0 or ci >= N or cj < 0 or cj >= M:
                res = 0
                break
            m = memo[ci][cj][cdir]
            if m is not None:
                res = m
                break
            key = (ci, cj, cdir)
            if key in visited:
                res = -1
                break
            visited[key] = len(path)
            path.append(key)
            cell = grid[ci][cj]
            if cell == '/':
                nd = slash_map[cdir]
            else:
                nd = back_map[cdir]
            di, dj = delta[nd]
            ci += di; cj += dj; cdir = nd
        for si, sj, sdir in reversed(path):
            if res == -1:
                memo[si][sj][sdir] = -1
            else:
                res += 1
                memo[si][sj][sdir] = res
        return res
    ans = 0
    for j in range(M):
        r = compute(0, j, 2)
        if r == -1:
            print(-1); return
        ans = max(ans, r)
        r = compute(N-1, j, 0)
        if r == -1:
            print(-1); return
        ans = max(ans, r)
    for i in range(N):
        r = compute(i, 0, 1)
        if r == -1:
            print(-1); return
        ans = max(ans, r)
        r = compute(i, M-1, 3)
        if r == -1:
            print(-1); return
        ans = max(ans, r)
    print(ans)

if __name__ == '__main__':
    main()
