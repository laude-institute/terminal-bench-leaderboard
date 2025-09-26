#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    # Read original figurine
    orig = []
    for _ in range(N):
        orig.append(next(it))
    orig_coords = {(r, c) for r in range(N) for c in range(N) if orig[r][c] == '#'}
    # Read pieces
    pieces = []
    for _ in range(K):
        grid = [next(it) for _ in range(N)]
        coords = [(r, c) for r in range(N) for c in range(N) if grid[r][c] == '#']
        pieces.append(coords)

    # Precompute placements for each piece
    placements = []  # list of list of sets
    for coords in pieces:
        if not coords:
            placements.append([])
            continue
        rs = [r for r, _ in coords]
        cs = [c for _, c in coords]
        min_r, max_r = min(rs), max(rs)
        min_c, max_c = min(cs), max(cs)
        valid = []
        # shifts dr, dc so piece stays within grid
        for dr in range(-min_r, N - max_r):
            for dc in range(-min_c, N - max_c):
                s = {(r + dr, c + dc) for r, c in coords}
                valid.append(s)
        placements.append(valid)

    # Try all pairs
    for i in range(K):
        for j in range(i + 1, K):
            for p1 in placements[i]:
                # early skip if p1 not subset of orig
                if not p1.issubset(orig_coords):
                    continue
                for p2 in placements[j]:
                    # Check disjoint and union match
                    if p1 & p2:
                        continue
                    if p1 | p2 == orig_coords:
                        # found
                        print(i+1, j+1)
                        return

if __name__ == '__main__':
    main()
