#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    idx = 1
    for _ in range(n):
        row = list(map(int, list(data[idx].strip())))
        grid.append(row)
        idx += 1

    # Collect visible colors and initialize bounding boxes
    visible = set()
    bounds = {c: [n, -1, n, -1] for c in range(1, 10)}  # c: [minr, maxr, minc, maxc]
    for i in range(n):
        for j in range(n):
            c = grid[i][j]
            if c > 0:
                visible.add(c)
                b = bounds[c]
                if i < b[0]: b[0] = i
                if i > b[1]: b[1] = i
                if j < b[2]: b[2] = j
                if j > b[3]: b[3] = j

    # Determine colors that cannot be first
    cannot_first = set()
    for c in visible:
        minr, maxr, minc, maxc = bounds[c]
        # If c appears, its bounds have been set
        for i in range(minr, maxr+1):
            for j in range(minc, maxc+1):
                d = grid[i][j]
                if d != c:
                    cannot_first.add(d)

    # Count possible first-painted colors
    possible = [c for c in visible if c not in cannot_first]
    print(len(possible))

if __name__ == '__main__':
    main()
