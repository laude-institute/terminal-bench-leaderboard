#!/usr/bin/env python3
"""
Compute the maximum area of a right triangle with legs parallel to axes
given N fence posts, outputting twice the area.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    coords = []
    idx = 1
    for i in range(n):
        x = int(data[idx]); y = int(data[idx+1])
        coords.append((x, y))
        idx += 2

    max_area2 = 0
    # For each point as the right-angle vertex
    for i in range(n):
        xi, yi = coords[i]
        max_dx = 0
        max_dy = 0
        # scan for horizontal and vertical legs
        for j in range(n):
            if j == i:
                continue
            xj, yj = coords[j]
            if yj == yi:
                # horizontal leg
                dx = abs(xj - xi)
                if dx > max_dx:
                    max_dx = dx
            if xj == xi:
                # vertical leg
                dy = abs(yj - yi)
                if dy > max_dy:
                    max_dy = dy
        # if both legs exist, update area2
        if max_dx > 0 and max_dy > 0:
            area2 = max_dx * max_dy
            if area2 > max_area2:
                max_area2 = area2

    # output twice the area (area2)
    print(max_area2)

if __name__ == '__main__':
    main()
