#!/usr/bin/env python3
import sys

def count_rectangles(grid, N, k):
    # Count sub-rectangles where all values >= k
    heights = [0] * N
    total = 0
    for i in range(N):
        # Update histogram heights
        for j in range(N):
            if grid[i][j] >= k:
                heights[j] += 1
            else:
                heights[j] = 0
        # Compute left limits using a monotonic stack
        stack = []  # pairs of (height, count)
        left = [0] * N
        for j in range(N):
            cnt = 1
            while stack and stack[-1][0] >= heights[j]:
                cnt += stack[-1][1]
                stack.pop()
            left[j] = cnt
            stack.append((heights[j], cnt))
        # Compute right limits using a monotonic stack
        stack = []
        right = [0] * N
        for j in range(N - 1, -1, -1):
            cnt = 1
            while stack and stack[-1][0] > heights[j]:
                cnt += stack[-1][1]
                stack.pop()
            right[j] = cnt
            stack.append((heights[j], cnt))
        # Sum contributions
        for j in range(N):
            total += heights[j] * left[j] * right[j]
    return total

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    grid = [[int(next(it)) for _ in range(N)] for _ in range(N)]
    # Use inclusion-exclusion: min == 100
    res = count_rectangles(grid, N, 100) - count_rectangles(grid, N, 101)
    print(res)

if __name__ == '__main__':
    main()
