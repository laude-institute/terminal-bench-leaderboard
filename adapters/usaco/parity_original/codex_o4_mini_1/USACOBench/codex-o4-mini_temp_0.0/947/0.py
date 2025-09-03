#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    A = [int(next(it)) for _ in range(2*n)]

    # Compute inversions in first half
    inv1 = 0
    ones = 0
    for i in range(n):
        if A[i] == 1:
            ones += 1
        else:
            inv1 += ones

    # Compute inversions in second half
    inv2 = 0
    ones = 0
    for i in range(n, 2*n):
        if A[i] == 1:
            ones += 1
        else:
            inv2 += ones

    diff = inv1 - inv2
    best = abs(diff)

    # Consider one boundary swap if bits differ
    if A[n-1] != A[n]:
        # ones in first half
        ones1 = sum(A[0:n])
        # zeros in second half
        zeros2 = n - sum(A[n:2*n])
        # c1: number of ones in first half excluding A[n-1]
        c1 = ones1 - (1 if A[n-1] == 1 else 0)
        # c0: number of zeros in second half excluding A[n]
        c0 = zeros2 - (1 if A[n] == 0 else 0)
        if A[n-1] == 0 and A[n] == 1:
            delta = c0 - c1
        else:
            delta = c1 - c0
        best = min(best, 1 + abs(diff + delta))

    print(best)

if __name__ == '__main__':
    main()
