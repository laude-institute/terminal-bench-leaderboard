#!/usr/bin/env python3
import sys

def main():
    # Read input
    N = int(sys.stdin.readline().strip())
    positions = [int(sys.stdin.readline().strip()) for _ in range(N)]
    positions.sort()

    # Compute minimum moves
    # Special case: nearly consecutive except one large gap at one end
    if (positions[N-2] - positions[0] == N-2 and positions[N-1] - positions[N-2] > 2) \
       or (positions[N-1] - positions[1] == N-2 and positions[1] - positions[0] > 2):
        min_moves = 2
    else:
        min_moves = N
        j = 0
        # Sliding window to find largest group fitting in N-length interval
        for i in range(N):
            while j + 1 < N and positions[j+1] - positions[i] + 1 <= N:
                j += 1
            cows_in_window = j - i + 1
            min_moves = min(min_moves, N - cows_in_window)

    # Compute maximum moves: move endpoint cows inward one at a time
    max_moves = max(
        positions[N-1] - positions[1],
        positions[N-2] - positions[0]
    ) - (N - 2)

    # Output results
    print(min_moves)
    print(max_moves)

if __name__ == "__main__":
    main()
