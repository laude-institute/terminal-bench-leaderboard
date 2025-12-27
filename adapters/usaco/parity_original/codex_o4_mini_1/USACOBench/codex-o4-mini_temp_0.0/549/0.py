#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    # Read input
    N = int(input())
    # Collect possible values for each variable
    vars_vals = {'B': [], 'E': [], 'S': [], 'I': [], 'G': [], 'O': [], 'M': []}
    for _ in range(N):
        v, val = input().split()
        vars_vals[v].append(int(val))

    # Precompute counts of each remainder mod 7 for each variable
    cnt = {}
    for v, lst in vars_vals.items():
        rem_counts = [0] * 7
        for value in lst:
            rem_counts[value % 7] += 1
        cnt[v] = rem_counts

    # DP over partial sums mod 7 for X, Y, Z
    # X = B + 2E + 2S + I
    # Y = G + O + E + S
    # Z = M + 2O
    dp = [[[0] * 7 for _ in range(7)] for __ in range(7)]
    dp[0][0][0] = 1

    # Define processing order and coefficients for (dx, dy, dz)
    order = [
        ('B', (1, 0, 0)),
        ('E', (2, 1, 0)),
        ('S', (2, 1, 0)),
        ('I', (1, 0, 0)),
        ('G', (0, 1, 0)),
        ('O', (0, 1, 2)),
        ('M', (0, 0, 1)),
    ]

    for var, (cx, cy, cz) in order:
        rem_counts = cnt[var]
        new_dp = [[[0] * 7 for _ in range(7)] for __ in range(7)]
        for x in range(7):
            for y in range(7):
                for z in range(7):
                    ways = dp[x][y][z]
                    if ways == 0:
                        continue
                    # Try each possible remainder for this variable
                    for r in range(7):
                        c = rem_counts[r]
                        if c == 0:
                            continue
                        nx = (x + cx * r) % 7
                        ny = (y + cy * r) % 7
                        nz = (z + cz * r) % 7
                        new_dp[nx][ny][nz] += ways * c
        dp = new_dp

    # Count assignments where product X*Y*Z is divisible by 7
    # which is true if any of X, Y, or Z is 0 mod 7
    result = 0
    for x in range(7):
        for y in range(7):
            for z in range(7):
                if x == 0 or y == 0 or z == 0:
                    result += dp[x][y][z]

    print(result)

if __name__ == '__main__':
    main()
