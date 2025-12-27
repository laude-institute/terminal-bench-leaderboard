#!/usr/bin/env python3
"""
Reads an original N x N figurine and K broken pieces (each N x N),
finds the two pieces that when shifted (no rotation/flip) and superimposed
exactly reconstruct the original with no overlap.
"""
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    orig = [input().rstrip() for _ in range(N)]
    # set of coordinates in original figurine
    orig_pos = {(r, c) for r in range(N) for c in range(N) if orig[r][c] == '#'}

    # read pieces
    pieces = []  # list of sets of (r,c)
    bounds = []  # list of (min_r, max_r, min_c, max_c)
    for _ in range(K):
        grid = [input().rstrip() for _ in range(N)]
        pos = {(r, c) for r in range(N) for c in range(N) if grid[r][c] == '#'}
        pieces.append(pos)
        if pos:
            rs = [r for r, _ in pos]
            cs = [c for _, c in pos]
            bounds.append((min(rs), max(rs), min(cs), max(cs)))
        else:
            bounds.append((0, -1, 0, -1))

    # try all pairs
    for i in range(K):
        pos1 = pieces[i]
        min_r1, max_r1, min_c1, max_c1 = bounds[i]
        # possible shifts for piece1: dr1, dc1
        for dr1 in range(-min_r1, N - max_r1):
            for dc1 in range(-min_c1, N - max_c1):
                # shifted positions of piece1
                s1 = {(r+dr1, c+dc1) for (r, c) in pos1}
                # must be subset of original
                if not s1 <= orig_pos:
                    continue
                # remaining positions to cover
                rem = orig_pos - s1
                # try second piece
                for j in range(i+1, K):
                    pos2 = pieces[j]
                    min_r2, max_r2, min_c2, max_c2 = bounds[j]
                    # quick size check
                    if len(pos2) != len(rem):
                        continue
                    # try shifts for piece2
                    for dr2 in range(-min_r2, N - max_r2):
                        for dc2 in range(-min_c2, N - max_c2):
                            s2 = {(r+dr2, c+dc2) for (r, c) in pos2}
                            # must match rem exactly
                            if s2 == rem:
                                # found solution
                                a, b = i+1, j+1
                                print(a, b)
                                return

if __name__ == '__main__':
    main()
