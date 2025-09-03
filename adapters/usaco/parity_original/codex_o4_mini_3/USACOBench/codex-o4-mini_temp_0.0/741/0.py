#!/usr/bin/env python3
"""
Problem: Given N spotty and N plain cow genomes of length M, find the shortest substring-length L such that
looking at any contiguous segment of length L in the genome distinguishes all spotty from plain cows.

Approach:
1. Binary search on length L from 1 to M.
2. For each L, slide a window of length L across positions 0..M-L.
   - Collect spotty substrings of length L in a set.
   - Check no plain substring of same window is in the set.
3. If any window is valid, L works; try smaller. Otherwise, try larger.

Pseudocode:
read N, M
read spotty list of N strings
read plain list of N strings
define works(L):
    for start in 0..M-L:
        seen = {substr of spotty at start..start+L}
        if no plain substr at start..start+L in seen:
            return True
    return False
binary search L in [1..M] using works(L)
print minimum L
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    spotty = data[2:2+N]
    plain = data[2+N:2+2*N]

    def works(L):
        # Check if any window of length L separates spotty and plain
        for i in range(M - L + 1):
            seen = set(s[i:i+L] for s in spotty)
            # if no collision with plain
            if all(p[i:i+L] not in seen for p in plain):
                return True
        return False

    lo, hi = 1, M
    ans = M
    while lo <= hi:
        mid = (lo + hi) // 2
        if works(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)

if __name__ == '__main__':
    main()
