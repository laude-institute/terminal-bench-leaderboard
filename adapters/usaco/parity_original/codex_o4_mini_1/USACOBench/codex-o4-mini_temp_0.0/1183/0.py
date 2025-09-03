#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    h = list(map(int, data[1:]))
    stack = []  # stores indices of cows
    ans = 0
    for j in range(n):
        # pop cows shorter than current
        while stack and h[stack[-1]] < h[j]:
            i = stack.pop()
            ans += (j - i + 1)
        # current cow can see the nearest taller to the left
        if stack:
            ans += (j - stack[-1] + 1)
        stack.append(j)
    # output result
    print(ans)

if __name__ == "__main__":
    main()
