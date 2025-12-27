#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        N = int(next(it))
        K = int(next(it))
        grid = [list(next(it).strip()) for _ in range(N)]
        # dp[i][j][k][d]: ways to reach (i,j) with k changes, last move d (0=down,1=right)
        # Initialize dp to zeros
        dp = [[[[0, 0] for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
        # Seed initial moves from (0,0)
        if grid[0][0] == 'H' or grid[N-1][N-1] == 'H':
            out_lines.append('0')
            continue
        # Move down
        if N > 1 and grid[1][0] == '.':
            dp[1][0][0][0] = 1
        # Move right
        if N > 1 and grid[0][1] == '.':
            dp[0][1][0][1] = 1
        # DP transitions
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 'H':
                    continue
                # Skip start cell
                if i == 0 and j == 0:
                    continue
                # Process all states
                for k in range(K+1):
                    for d in (0, 1):
                        ways = dp[i][j][k][d]
                        if ways == 0:
                            continue
                        # Move down
                        ni, nj = i+1, j
                        if ni < N and grid[ni][nj] == '.':
                            if d == 0:
                                dp[ni][nj][k][0] += ways
                            elif k < K:
                                dp[ni][nj][k+1][0] += ways
                        # Move right
                        ni, nj = i, j+1
                        if nj < N and grid[ni][nj] == '.':
                            if d == 1:
                                dp[ni][nj][k][1] += ways
                            elif k < K:
                                dp[ni][nj][k+1][1] += ways
        # Sum up ways at destination
        total = 0
        for k in range(K+1):
            total += dp[N-1][N-1][k][0] + dp[N-1][N-1][k][1]
        out_lines.append(str(total))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
