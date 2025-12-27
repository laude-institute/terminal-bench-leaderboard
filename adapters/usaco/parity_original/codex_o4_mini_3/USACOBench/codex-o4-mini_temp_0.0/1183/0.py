#!/usr/bin/env python3
"""
Compute sum of distances between all pairs of cows that can toss a frisbee
if all cows in between are shorter than both ends.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    result = 0
    # Next greater to the right for each index
    stack = []  # stores indices with decreasing heights
    for i, hi in enumerate(h):
        while stack and h[stack[-1]] < hi:
            idx = stack.pop()
            result += (i - idx + 1)
        stack.append(i)
    # Previous greater to the left for each index
    stack = []
    for i, hi in enumerate(h):
        while stack and h[stack[-1]] < hi:
            stack.pop()
        if stack:
            idx = stack[-1]
            result += (i - idx + 1)
        stack.append(i)
    print(result)

if __name__ == '__main__':
    main()
