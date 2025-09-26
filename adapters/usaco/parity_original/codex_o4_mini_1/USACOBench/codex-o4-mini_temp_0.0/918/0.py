#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    pos = list(map(int, data[1:]))
    pos.sort()
    # Compute minimum moves via sliding window
    j = 0
    max_k = 0
    for i in range(N):
        while j + 1 < N and pos[j+1] - pos[i] + 1 <= N:
            j += 1
        max_k = max(max_k, j - i + 1)
    min_moves = N - max_k
    # Special case for two-move scenario
    if (pos[N-2] - pos[0] == N-2 and pos[N-1] - pos[N-2] > 2) or \
       (pos[N-1] - pos[1] == N-2 and pos[1] - pos[0] > 2):
        min_moves = 2
    # Compute maximum moves based on largest gaps
    max_moves = max(
        pos[N-1] - pos[1] - (N-2),
        pos[N-2] - pos[0] - (N-2)
    )
    # Output results
    print(min_moves)
    print(max_moves)

if __name__ == '__main__':
    main()
