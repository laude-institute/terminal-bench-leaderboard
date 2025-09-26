#!/usr/bin/env python3
"""
Determine if a fence path described by NESW directions is clockwise or counterclockwise.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    for _ in range(n):
        s = next(it)
        # Track fence vertices
        x = y = 0
        verts = [(x, y)]
        for c in s:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            verts.append((x, y))
        # Compute signed area (shoelace) * 2
        area2 = 0
        for i in range(len(verts) - 1):
            x0, y0 = verts[i]
            x1, y1 = verts[i + 1]
            area2 += x0 * y1 - x1 * y0
        # Positive area => CCW, Negative => CW
        if area2 > 0:
            print("CCW")
        else:
            print("CW")

if __name__ == '__main__':
    main()
