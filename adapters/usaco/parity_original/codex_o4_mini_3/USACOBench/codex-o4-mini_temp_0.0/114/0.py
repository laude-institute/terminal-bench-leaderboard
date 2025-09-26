#!/usr/bin/env python3
"""
Solution to the Moo sequence problem.
Generates lengths until covering N, then recursively finds the Nth character.
"""
import sys

def main():
    N = int(sys.stdin.readline().strip())
    # Build length sequence until we cover N
    lengths = [3]
    k = 0
    while lengths[k] < N:
        k += 1
        lengths.append(lengths[k-1] * 2 + (k + 3))

    def find_char(n, k):
        # Base case: S(0) = 'moo'
        if k == 0:
            return 'm' if n == 1 else 'o'
        left_len = lengths[k-1]
        mid_len = k + 3
        if n <= left_len:
            return find_char(n, k-1)
        elif n > left_len + mid_len:
            return find_char(n - left_len - mid_len, k-1)
        else:
            # In the middle segment
            return 'm' if n - left_len == 1 else 'o'

    # Compute and print the answer
    result = find_char(N, k)
    print(result)

if __name__ == '__main__':
    main()
