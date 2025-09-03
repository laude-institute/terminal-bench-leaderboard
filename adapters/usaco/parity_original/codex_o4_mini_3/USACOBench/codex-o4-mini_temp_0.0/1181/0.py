#!/usr/bin/env python3
"""
Solution to Farmer John corn feeding problem.
"""
import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        N = int(next(it))
        h = [int(next(it)) for _ in range(N)]
        # Handle small N directly
        if N == 1:
            out.append('0')
            continue
        if N == 2:
            out.append('0' if h[0] == h[1] else '-1')
            continue
        # Build alternating prefix array a of length N-1
        a = [0] * (N-1)
        a[0] = h[0]
        possible = True
        # Compute a[i] = h[i] - a[i-1]
        for i in range(1, N-1):
            a[i] = h[i] - a[i-1]
            # For even positions (1-based), a[i]>=0 must hold
            if i % 2 == 1 and a[i] < 0:
                possible = False
        if not possible:
            out.append('-1')
            continue
        # Determine final hunger t
        if N % 2 == 0:
            # Consistency: last prefix must equal last hunger
            if a[N-2] != h[N-1]:
                out.append('-1')
                continue
            # Maximize t so that odd-indexed ops non-negative
            # i%2==0 corresponds to 1-based odd positions
            t = min(a[i] for i in range(0, N-1, 2))
            if t < 0:
                out.append('-1')
                continue
        else:
            # Unique t from last equation
            t = h[N-1] - a[N-2]
            if t < 0:
                out.append('-1')
                continue
            # Ensure odd positions have enough a[i]
            for i in range(0, N-1, 2):
                if a[i] < t:
                    possible = False
                    break
            if not possible:
                out.append('-1')
                continue
        # Compute total operations
        ops = 0
        for i in range(N-1):
            if i % 2 == 0:
                ops += a[i] - t
            else:
                ops += a[i]
        # Each operation uses two bags
        out.append(str(2 * ops))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    solve()
