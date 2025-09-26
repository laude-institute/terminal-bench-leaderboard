#!/usr/bin/env python3
"""
Maximize number of cow-cow friendships via adjacent grass cells.
Approach: greedy assign each grass (with >=2 adjacent cows) a unique cow-pair,
processing grasses with fewer options first.
"""
import sys

def main():
    data = sys.stdin
    N, M = map(int, data.readline().split())
    grid = [data.readline().rstrip() for _ in range(N)]
    # helper for cow IDs
    # cow id = i*M + j
    grasses = {2: [], 3: [], 4: []}
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 'G':
                continue
            # collect neighbor cows
            neigh = []
            if i > 0 and grid[i-1][j] == 'C': neigh.append((i-1)*M + j)
            if i+1 < N and grid[i+1][j] == 'C': neigh.append((i+1)*M + j)
            if j > 0 and grid[i][j-1] == 'C': neigh.append(i*M + (j-1))
            if j+1 < M and grid[i][j+1] == 'C': neigh.append(i*M + (j+1))
            d = len(neigh)
            if d >= 2:
                # only need up to 4
                grasses[d].append(neigh)
    # track used cow-pairs
    used = set()
    res = 0
    # process grasses by neighbor count
    import itertools
    for d in (2, 3, 4):
        for neigh in grasses[d]:
            # try all cow-pairs for this grass
            found = False
            for u, v in itertools.combinations(neigh, 2):
                if u > v:
                    u, v = v, u
                if (u, v) not in used:
                    used.add((u, v))
                    res += 1
                    found = True
                    break
            # if none available, skip
    print(res)

if __name__ == '__main__':
    main()
