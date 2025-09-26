#!/usr/bin/env python3
"""
Count subrectangles with minimum exactly 100.
"""
import sys

def sum_subarray_mins(arr):
    n = len(arr)
    prev_less = [0] * n
    next_less_equal = [0] * n
    stack = []
    # Previous less element
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        prev_less[i] = stack[-1] if stack else -1
        stack.append(i)
    # Next less or equal element
    stack.clear()
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        next_less_equal[i] = stack[-1] if stack else n
        stack.append(i)
    # Sum contributions
    total = 0
    for i in range(n):
        left_count = i - prev_less[i]
        right_count = next_less_equal[i] - i
        total += arr[i] * left_count * right_count
    return total

def count_at_least(grid, n, threshold):
    heights = [0] * n
    total = 0
    for i in range(n):
        row = grid[i]
        for j in range(n):
            # build histogram of consecutive >= threshold
            if row[j] >= threshold:
                heights[j] += 1
            else:
                heights[j] = 0
        total += sum_subarray_mins(heights)
    return total

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = []
    for _ in range(n):
        row = [int(next(it)) for _ in range(n)]
        grid.append(row)
    # count subrectangles with min exactly 100 = f(100) - f(101)
    total = count_at_least(grid, n, 100) - count_at_least(grid, n, 101)
    print(total)

if __name__ == '__main__':
    main()
