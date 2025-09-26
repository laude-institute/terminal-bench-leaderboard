#!/usr/bin/env python3
import sys

def can_place(existing, N, D):
    # Check existing cows distance
    for i in range(len(existing) - 1):
        if existing[i+1] - existing[i] < D:
            return False
    # Compute free segments where new cows can go
    total = 0
    # Prefix
    p0 = existing[0]
    Lp = p0 - D + 1
    if Lp > 0:
        total += (Lp - 1) // D + 1
    # Middle gaps
    for i in range(len(existing) - 1):
        gap = existing[i+1] - existing[i] - 1
        Lm = gap - 2 * (D - 1)
        if Lm > 0:
            total += (Lm - 1) // D + 1
    # Suffix
    pk = existing[-1]
    Ls = N - pk - D
    if Ls > 0:
        total += (Ls - 1) // D + 1
    return total >= 2

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    s = data[1].strip()
    existing = [i for i, c in enumerate(s) if c == '1']
    # If no cows, place at ends
    if not existing:
        print(N-1)
        return
    # Binary search on D
    lo, hi = 1, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_place(existing, N, mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == '__main__':
    main()
