#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    coords = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1])
        coords.append((x, y))
        idx += 2

    ans = 0
    # For each point as a right angle vertex
    for i in range(n):
        xi, yi = coords[i]
        max_dx = 0
        max_dy = 0
        # Find farthest horizontal and vertical distances
        for xj, yj in coords:
            if yj == yi:
                dx = abs(xj - xi)
                if dx > max_dx:
                    max_dx = dx
            if xj == xi:
                dy = abs(yj - yi)
                if dy > max_dy:
                    max_dy = dy
        # Twice the area is product of legs
        area2 = max_dx * max_dy
        if area2 > ans:
            ans = area2

    print(ans)

if __name__ == "__main__":
    main()
