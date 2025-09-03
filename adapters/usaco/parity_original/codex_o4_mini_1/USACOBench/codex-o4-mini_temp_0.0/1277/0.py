#!/usr/bin/env python3
"""
Solution for transforming a string of 'M' and 'O' into "MOO"
using minimum end-deletions and end-flips.
"""
import sys

def main():
    input = sys.stdin.readline
    Q_line = input().strip()
    if not Q_line:
        return
    Q = int(Q_line)
    for _ in range(Q):
        s = input().strip()
        n = len(s)
        # Cannot form "MOO" if shorter than 3
        if n < 3:
            print(-1)
            continue
        # Base deletions: remove n-3 characters to reach length 3
        base_ops = n - 3
        best = float('inf')
        # Only contiguous substrings of length 3 are reachable
        for i in range(n - 2):
            # Middle character must be 'O' (cannot flip middle)
            if s[i+1] != 'O':
                continue
            # Count flips for first and last chars
            flips = (0 if s[i] == 'M' else 1) + (0 if s[i+2] == 'O' else 1)
            best = min(best, base_ops + flips)
        # If no valid substring found, impossible
        print(best if best != float('inf') else -1)

if __name__ == '__main__':
    main()
