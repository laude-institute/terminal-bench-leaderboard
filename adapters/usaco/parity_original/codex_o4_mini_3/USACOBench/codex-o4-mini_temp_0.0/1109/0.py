#!/usr/bin/env python3
"""
Determine orientation (CW or CCW) of a simple closed fence path.
Moves are given as a string of N, E, S, W steps of unit length.
Compute signed area via the shoelace formula on the traced vertices.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    idx = 1
    for _ in range(n):
        path = data[idx]
        idx += 1
        x, y = 0, 0
        vertices = [(x, y)]
        # Trace the path and record vertices
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            vertices.append((x, y))
        # Compute twice the signed area
        area2 = 0
        for (x0, y0), (x1, y1) in zip(vertices, vertices[1:]):
            area2 += x0 * y1 - x1 * y0
        # area2 > 0 => CCW, else CW
        if area2 > 0:
            print("CCW")
        else:
            print("CW")

if __name__ == '__main__':
    main()
