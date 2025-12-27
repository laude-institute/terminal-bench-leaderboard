#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Read grid and mark cow positions
    grid = [input().strip() for _ in range(N)]
    has_cow = [[c == '*' for c in row] for row in grid]
    # Prepare lists of cow positions by row, column, and diagonals
    row_list = [[] for _ in range(N)]
    col_list = [[] for _ in range(N)]
    diag1_list = [[] for _ in range(2 * N - 1)]  # i - j = const
    diag2_list = [[] for _ in range(2 * N - 1)]  # i + j = const
    for i in range(N):
        for j in range(N):
            if has_cow[i][j]:
                row_list[i].append(j)
                col_list[j].append(i)
                diag1_list[i - j + N - 1].append(i)
                diag2_list[i + j].append(i)
    # Sort lists for ordered pair enumeration
    for lst in row_list + col_list + diag1_list + diag2_list:
        lst.sort()

    count = 0
    # Horizontal bases (row-wise)
    for i in range(N):
        cols = row_list[i]
        L = len(cols)
        for a in range(L):
            j1 = cols[a]
            for b in range(a + 1, L):
                j2 = cols[b]
                delta = j2 - j1
                if delta & 1:
                    continue
                d = delta >> 1
                m = j1 + d
                up = i - d
                if up >= 0 and has_cow[up][m]:
                    count += 1
                down = i + d
                if down < N and has_cow[down][m]:
                    count += 1

    # Vertical bases (column-wise)
    for j in range(N):
        rows = col_list[j]
        L = len(rows)
        for a in range(L):
            i1 = rows[a]
            for b in range(a + 1, L):
                i2 = rows[b]
                delta = i2 - i1
                if delta & 1:
                    continue
                d = delta >> 1
                m = i1 + d
                left = j - d
                if left >= 0 and has_cow[m][left]:
                    count += 1
                right = j + d
                if right < N and has_cow[m][right]:
                    count += 1

    # Diagonal bases with slope +1 (i - j = const)
    for k in range(2 * N - 1):
        is_ = diag1_list[k]
        diff = k - (N - 1)
        L = len(is_)
        for a in range(L):
            i1 = is_[a]
            j1 = i1 - diff
            for b in range(a + 1, L):
                i2 = is_[b]
                delta = i2 - i1
                if delta & 1:
                    continue
                j2 = i2 - diff
                # Apex positions: (i2, j1) and (i1, j2)
                if has_cow[i2][j1]:
                    count += 1
                if has_cow[i1][j2]:
                    count += 1

    # Diagonal bases with slope -1 (i + j = const)
    for k in range(2 * N - 1):
        is_ = diag2_list[k]
        L = len(is_)
        for a in range(L):
            i1 = is_[a]
            j1 = k - i1
            for b in range(a + 1, L):
                i2 = is_[b]
                delta = i2 - i1
                if delta & 1:
                    continue
                j2 = k - i2
                # Apex positions: (i2, j1) and (i1, j2)
                if has_cow[i2][j1]:
                    count += 1
                if has_cow[i1][j2]:
                    count += 1

    print(count)

if __name__ == '__main__':
    main()
