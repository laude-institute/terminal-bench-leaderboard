#!/usr/bin/env python3
import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        N = int(next(it)); K = int(next(it))
        grid = [list(next(it).strip()) for _ in range(N)]
        # dp[i][j][k][d]: ways to reach (i,j) with k direction changes, last move d (0=R,1=D)
        dp = [[[[0]*2 for _ in range(K+1)] for _ in range(N)] for __ in range(N)]
        # Initialize first moves from (0,0)
        if N > 1:
            # move right to (0,1)
            if grid[0][1] == '.':
                dp[0][1][0][0] = 1
            # move down to (1,0)
            if grid[1][0] == '.':
                dp[1][0][0][1] = 1
        # Fill DP
        for i in range(N):
            for j in range(N):
                if (i == 0 and j <= 1) or (j == 0 and i <= 1):
                    # Skip starting cell and its immediate neighbors (initialized)
                    continue
                if grid[i][j] != '.':
                    continue
                for k in range(K+1):
                    # last move is right (from left)
                    if j > 0 and grid[i][j-1] == '.':
                        # continue right
                        dp[i][j][k][0] += dp[i][j-1][k][0]
                        # turn from down to right
                        if k > 0:
                            dp[i][j][k][0] += dp[i][j-1][k-1][1]
                    # last move is down (from above)
                    if i > 0 and grid[i-1][j] == '.':
                        # continue down
                        dp[i][j][k][1] += dp[i-1][j][k][1]
                        # turn from right to down
                        if k > 0:
                            dp[i][j][k][1] += dp[i-1][j][k-1][0]
        # Sum up ways to reach (N-1,N-1)
        total = 0
        for k in range(K+1):
            total += dp[N-1][N-1][k][0] + dp[N-1][N-1][k][1]
        out.append(str(total))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    solve()
