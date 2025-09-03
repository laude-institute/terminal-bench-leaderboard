#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    vals = list(map(int, data[1:]))
    # build grid
    grid = [vals[i*n:(i+1)*n] for i in range(n)]
    total = 0
    # pair rows (0-based) in steps of 2
    for i in range(0, n, 2):
        row1 = grid[i]
        row2 = grid[i+1]
        # for each column, choose max in the pair
        for j in range(n):
            # place cow in the cell with higher beauty
            total += max(row1[j], row2[j])
    print(total)

if __name__ == "__main__":
    main()
