#!/usr/bin/env python3
"""Solution to 'Partitioning the Farm' problem."""
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    grid = [[int(next(it)) for _ in range(N)] for _ in range(N)]

    # 2D prefix sum
    psum = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j] - psum[i][j] + grid[i][j]

    def rect_sum(r1, r2, c):
        # sum rows r1..r2 at column c
        return psum[r2+1][c+1] - psum[r1][c+1] - psum[r2+1][c] + psum[r1][c]

    # Check if possible with max block sum <= M
    def feasible(M):
        # iterate horizontal cut masks
        for mask in range(1<<(N-1)):
            h_cuts = mask.bit_count()
            if h_cuts > K:
                continue
            # build row groups
            groups = []
            rs = 0
            for i in range(N-1):
                if mask & (1<<i):
                    groups.append((rs, i))
                    rs = i+1
            groups.append((rs, N-1))
            G = len(groups)
            # precompute block sums per group per column
            gs = [[0]*N for _ in range(G)]
            ok = True
            for gi, (r1, r2) in enumerate(groups):
                for c in range(N):
                    s = rect_sum(r1, r2, c)
                    if s > M:
                        ok = False
                        break
                    gs[gi][c] = s
                if not ok:
                    break
            if not ok:
                continue
            # greedily place vertical cuts
            v_cuts = 0
            cur = [0]*G
            for c in range(N):
                for gi in range(G):
                    cur[gi] += gs[gi][c]
                if any(cur[gi] > M for gi in range(G)):
                    v_cuts += 1
                    cur = [gs[gi][c] for gi in range(G)]
                if h_cuts + v_cuts > K:
                    break
            if h_cuts + v_cuts <= K:
                return True
        return False

    # binary search on answer
    low = max(max(row) for row in grid)
    high = sum(sum(row) for row in grid)
    while low < high:
        mid = (low + high)//2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    main()
