#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n_line = data.readline().strip()
    if not n_line:
        return
    n = int(n_line)
    h = list(map(int, data.readline().split()))
    # Arrays for nearest greater to left and right
    L = [-1] * n
    R = [-1] * n
    stack = []  # stack of indices
    # Compute next greater to right for each position
    for i in range(n):
        while stack and h[stack[-1]] < h[i]:
            idx = stack.pop()
            R[idx] = i
        stack.append(i)
    # Compute previous greater to left for each position
    stack.clear()
    for i in range(n):
        while stack and h[stack[-1]] <= h[i]:
            stack.pop()
        L[i] = stack[-1] if stack else -1
        stack.append(i)
    # Sum distances for valid pairs
    total = 0
    # Pairs where current has a greater to the right
    for i in range(n):
        if R[i] != -1:
            total += (R[i] - i + 1)
    # Pairs where current has a greater to the left
    for i in range(n):
        if L[i] != -1:
            total += (i - L[i] + 1)
    print(total)

if __name__ == "__main__":
    main()
