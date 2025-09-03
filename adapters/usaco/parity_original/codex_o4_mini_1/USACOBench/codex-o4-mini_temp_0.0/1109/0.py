#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    idx = 1
    for _ in range(n):
        path = data[idx]
        idx += 1
        x = y = 0
        # Collect vertices of the fence path
        vertices = [(0, 0)]
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
        # Compute signed area via shoelace sum
        s = 0
        for i in range(len(vertices) - 1):
            x1, y1 = vertices[i]
            x2, y2 = vertices[i + 1]
            s += x1 * y2 - x2 * y1
        # Negative area => clockwise, positive => counter-clockwise
        if s < 0:
            print('CW')
        else:
            print('CCW')

if __name__ == '__main__':
    main()
