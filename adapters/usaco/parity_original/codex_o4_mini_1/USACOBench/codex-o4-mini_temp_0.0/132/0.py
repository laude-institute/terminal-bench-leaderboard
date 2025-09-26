#!/usr/bin/env python3
"""
Compute the maximum number of islands in a 1D landscape
as water rises, using reverse union logic.
"""
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    H = [int(input()) for _ in range(n)]
    # Sort positions by descending height
    heights_idx = sorted(range(n), key=lambda i: -H[i])
    visited = [False] * n
    islands = 0
    result = 0
    # Add land back from highest to lowest
    for i in heights_idx:
        visited[i] = True
        islands += 1
        # Merge with adjacent islands if present
        if i > 0 and visited[i-1]:
            islands -= 1
        if i < n-1 and visited[i+1]:
            islands -= 1
        if islands > result:
            result = islands
    print(result)

if __name__ == "__main__":
    main()
