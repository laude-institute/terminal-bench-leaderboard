#!/usr/bin/env python3
"""
Reconstruct the lexicographically minimum permutation a of 1..N
given adjacent sums b_i = a_i + a_{i+1}.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    b = list(map(int, input().split()))
    # Try each possible first element in increasing order
    for first in range(1, N+1):
        a = [first]
        valid = True
        # Build the permutation based on sums
        for bi in b:
            nxt = bi - a[-1]
            # Check bounds
            if nxt < 1 or nxt > N:
                valid = False
                break
            a.append(nxt)
        # Verify it's a valid permutation
        if not valid:
            continue
        if len(set(a)) == N:
            print(" ".join(map(str, a)))
            return

if __name__ == '__main__':
    main()
