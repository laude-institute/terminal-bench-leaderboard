#!/usr/bin/env python3
"""
Solution for uniform cow orientation with one possible bad cow.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    # Read grid, convert R->0, L->1; use 1-based indexing
    A = [[0]*(N+1)]
    for _ in range(N):
        row = next(it).strip()
        A.append([0] + [1 if ch == 'L' else 0 for ch in row])

    # Compute consistency matrix C for i,j >= 2
    # C[i][j] = A[i][j] ^ A[1][j] ^ A[i][1] ^ A[1][1]
    total = 0
    row_counts = [0] * (N+1)
    col_counts = [0] * (N+1)
    for i in range(2, N+1):
        for j in range(2, N+1):
            c = A[i][j] ^ A[1][j] ^ A[i][1] ^ A[1][1]
            if c:
                total += 1
                row_counts[i] += 1
                col_counts[j] += 1

    # Case 1: single inconsistent cell at (p,q) for p>1,q>1
    if total == 1:
        for i in range(2, N+1):
            for j in range(2, N+1):
                if (A[i][j] ^ A[1][j] ^ A[i][1] ^ A[1][1]) == 1:
                    print(i, j)
                    return

    # Case 2: one bad column or one bad row involving first row/column
    if total == N-1:
        # bad column at (1, q)
        for j in range(2, N+1):
            if col_counts[j] == N-1:
                print(1, j)
                return
        # bad row at (p, 1)
        for i in range(2, N+1):
            if row_counts[i] == N-1:
                print(i, 1)
                return

    # Case 3: all cells inconsistent => bad at (1,1)
    if total == (N-1) * (N-1):
        print(1, 1)
        return

    # No solution
    print(-1)

if __name__ == '__main__':
    main()
