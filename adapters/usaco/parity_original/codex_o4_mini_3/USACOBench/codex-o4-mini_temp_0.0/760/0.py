#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Read shuffle mapping; a[i] is destination of cow at position i
    A = list(map(int, input().split()))
    # Read final arrangement of cow IDs after three shuffles
    cows = list(map(int, input().split()))
    # Convert mapping to 0-based indices
    A = [x - 1 for x in A]
    # Compute inverse mapping: inv[j] = i where A[i] == j
    inv = [0] * N
    for i, dest in enumerate(A):
        inv[dest] = i
    # Apply inverse shuffle three times to recover initial order
    for _ in range(3):
        prev = [0] * N
        for pos in range(N):
            prev[pos] = cows[inv[pos]]
        cows = prev
    # Output the initial order, one ID per line
    for cid in cows:
        print(cid)

if __name__ == "__main__":
    main()
