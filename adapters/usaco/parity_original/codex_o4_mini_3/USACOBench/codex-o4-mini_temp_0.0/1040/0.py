#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    n = int(next(it))
    pts = []
    for _ in range(n):
        x = int(next(it)); y = int(next(it))
        pts.append((x, y))
    pts.sort(key=lambda p: (p[0], p[1]))
    stack = []  # minimal y for each component
    comp = 0
    for x, y in pts:
        comp += 1
        m = y
        # merge all components with minimal_y <= y
        while stack and stack[-1] <= y:
            m = stack[-1] if stack[-1] < m else m
            stack.pop()
            comp -= 1
        # now m is minimal y of merged comp
        stack.append(m)
    # comp is number of components
    sys.stdout.write(str(comp))

if __name__ == '__main__':
    main()
