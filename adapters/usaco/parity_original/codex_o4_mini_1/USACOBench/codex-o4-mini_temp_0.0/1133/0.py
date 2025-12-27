#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N, M = map(int, data.readline().split())
    grid = [data.readline().strip() for _ in range(N)]
    # Directions: up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    eligible = 0
    # Count forced duplicate pairs for grasses with exactly two neighbors
    pair_counts = {}
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 'G':
                continue
            cows = []
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 'C':
                    cows.append(ni * M + nj)
            k = len(cows)
            if k < 2:
                continue
            eligible += 1
            if k == 2:
                a, b = cows
                if a > b:
                    a, b = b, a
                pair_counts[(a, b)] = pair_counts.get((a, b), 0) + 1
    # Total duplicates to remove: for each forced pair, at most one use
    remove = 0
    for cnt in pair_counts.values():
        if cnt > 1:
            remove += cnt - 1
    # Answer is eligible grasses minus forced duplicates
    print(eligible - remove)

if __name__ == '__main__':
    main()
