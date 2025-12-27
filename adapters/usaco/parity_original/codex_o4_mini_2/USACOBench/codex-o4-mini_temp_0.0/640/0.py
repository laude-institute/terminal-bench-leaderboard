#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    # Read original grid
    orig = set()
    for r in range(N):
        line = next(it)
        for c, ch in enumerate(line):
            if ch == '#':
                orig.add((r, c))

    # Read pieces
    pieces = []  # list of lists of coords
    shifts = []  # list of possible shifts per piece
    for _ in range(K):
        coords = []
        minr, minc = N, N
        maxr = maxc = -1
        for r in range(N):
            line = next(it)
            for c, ch in enumerate(line):
                if ch == '#':
                    coords.append((r, c))
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)
        pieces.append(coords)
        # compute allowed shifts so piece remains within grid
        d_rs = range(-minr, N - maxr)
        d_cs = range(-minc, N - maxc)
        shifts.append([(dr, dc) for dr in d_rs for dc in d_cs])

    # Try all pairs
    for i in range(K):
        coords_i = pieces[i]
        for j in range(i+1, K):
            coords_j = pieces[j]
            # try shifts
            for dr1, dc1 in shifts[i]:
                # shift piece i
                si = {(r+dr1, c+dc1) for r, c in coords_i}
                # must be subset of orig
                if not si.issubset(orig):
                    continue
                for dr2, dc2 in shifts[j]:
                    sj = {(r+dr2, c+dc2) for r, c in coords_j}
                    # subset and no overlap
                    if not sj.issubset(orig):
                        continue
                    if si & sj:
                        continue
                    # union equals orig?
                    if si | sj == orig:
                        print(i+1, j+1)
                        return

if __name__ == '__main__':
    main()
