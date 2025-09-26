#!/usr/bin/env python3
"""
Solution to the Islands problem (USACO 2012).
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Read heights
    H = [int(input()) for _ in range(N)]
    # Sort positions by descending height
    arr = sorted([(h, i) for i, h in enumerate(H)], key=lambda x: -x[0])
    seen = [False] * N
    curr = 0
    max_islands = 0
    i = 0
    # Process by height groups
    while i < N:
        height = arr[i][0]
        # Add all land of this height
        j = i
        while j < N and arr[j][0] == height:
            idx = arr[j][1]
            seen[idx] = True
            curr += 1
            # Merge with left neighbor if present
            if idx - 1 >= 0 and seen[idx - 1]:
                curr -= 1
            # Merge with right neighbor if present
            if idx + 1 < N and seen[idx + 1]:
                curr -= 1
            j += 1
        # Update maximum islands after batch
        if curr > max_islands:
            max_islands = curr
        i = j
    # Output result
    print(max_islands)

if __name__ == '__main__':
    main()
