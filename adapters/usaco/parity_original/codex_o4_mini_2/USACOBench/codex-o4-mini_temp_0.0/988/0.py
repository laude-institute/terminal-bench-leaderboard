#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    b = list(map(int, data[1:]))
    # Try each possible first element for lexicographically smallest
    for first in range(1, n+1):
        a = [0] * n
        used = [False] * (n + 1)
        a[0] = first
        if first > n:
            continue
        used[first] = True
        valid = True
        # Reconstruct the permutation
        for i in range(1, n):
            a[i] = b[i-1] - a[i-1]
            # Check bounds and uniqueness
            if a[i] <= 0 or a[i] > n or used[a[i]]:
                valid = False
                break
            used[a[i]] = True
        # Check if valid and complete
        if valid:
            # Found lexicographically smallest valid permutation
            print(' '.join(map(str, a)))
            return

if __name__ == '__main__':
    main()
