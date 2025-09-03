#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    idx = 1
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i] = int(data[idx]); idx += 1
    for i in range(1, N + 1):
        B[i] = int(data[idx]); idx += 1

    # Build position maps
    posA = [0] * (N + 1)
    posB = [0] * (N + 1)
    for i in range(1, N + 1):
        posA[A[i]] = i
        posB[B[i]] = i

    # Build cow-to-cow mapping for cycles
    mapping = [0] * (N + 1)
    for c in range(1, N + 1):
        target_pos = posB[c]
        mapping[c] = A[target_pos]

    visited = [False] * (N + 1)
    cycles = 0
    max_len = 0

    # Find cycles
    for c in range(1, N + 1):
        if not visited[c] and posA[c] != posB[c]:
            length = 0
            curr = c
            while not visited[curr]:
                visited[curr] = True
                curr = mapping[curr]
                length += 1
            cycles += 1
            if length > max_len:
                max_len = length

    if cycles == 0:
        max_len = -1

    print(cycles, max_len)

if __name__ == "__main__":
    main()
