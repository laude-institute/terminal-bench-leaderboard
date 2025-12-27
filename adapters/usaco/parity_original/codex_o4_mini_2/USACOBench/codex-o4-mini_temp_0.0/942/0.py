#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    grid = data[1:]
    # Map 'R' to 1, 'L' to 0
    b = [[1 if c == 'R' else 0 for c in row] for row in grid]
    M = 0  # total mismatches in d matrix
    sub_count = 0  # mismatches in submatrix i>=2,j>=2 (0-based i>=1,j>=1)
    row_count = [0] * N  # counts per row i>=2 (i>=1)
    col_count = [0] * N  # counts per col j>=2 (j>=1)
    uniquex = -1
    uniquey = -1
    b00 = b[0][0]
    # Compute d[i][j] = b[i][j] ^ b[0][j] ^ b[i][0] ^ b[0][0]
    for i in range(N):
        for j in range(N):
            d = b[i][j] ^ b[0][j] ^ b[i][0] ^ b00
            if d:
                M += 1
                if i >= 1 and j >= 1:
                    sub_count += 1
                    row_count[i] += 1
                    col_count[j] += 1
                    uniquex, uniquey = i, j
    best = (N+1, N+1)
    # Candidate at (1,1)
    if 2 * sub_count == M + (N-1)*(N-1):
        best = (0, 0)
    # Candidate at (1,y) and (x,1)
    target = M + N - 1
    if target % 2 == 0:
        for j in range(1, N):
            if 2 * col_count[j] == target:
                best = min(best, (0, j))
                break
        for i in range(1, N):
            if 2 * row_count[i] == target:
                best = min(best, (i, 0))
                break
    # Candidate in submatrix when single mismatch
    if M == 1 and uniquex >= 1 and uniquey >= 1:
        best = min(best, (uniquex, uniquey))
    # Output result
    if best[0] <= N-1:
        # convert to 1-based
        print(best[0] + 1, best[1] + 1)
    else:
        print(-1)

if __name__ == "__main__":
    main()
