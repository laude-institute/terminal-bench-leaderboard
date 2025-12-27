#!/usr/bin/env python3
import sys

def sum_subarray_mins(A):
    n = len(A)
    left = [0] * n
    right = [0] * n
    stack = []
    # previous less element (strictly less)
    for i in range(n):
        while stack and A[stack[-1]] > A[i]:
            stack.pop()
        left[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    # next less or equal element
    stack.clear()
    for i in range(n-1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        right[i] = n - i if not stack else stack[-1] - i
        stack.append(i)
    total = 0
    for i in range(n):
        total += A[i] * left[i] * right[i]
    return total

def count_rects(grid, N, threshold):
    heights = [0] * N
    total = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] >= threshold:
                heights[j] += 1
            else:
                heights[j] = 0
        total += sum_subarray_mins(heights)
    return total

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    vals = list(map(int, data[1:]))
    grid = [vals[i*N:(i+1)*N] for i in range(N)]
    # Count sub-grids with min exactly 100
    cnt100 = count_rects(grid, N, 100)
    cnt101 = count_rects(grid, N, 101)
    print(cnt100 - cnt101)

if __name__ == '__main__':
    main()
