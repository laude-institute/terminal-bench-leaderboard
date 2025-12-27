#!/usr/bin/env python3
"""
Reads N fence post coordinates and computes the maximum twice-area of a right triangle
with one leg parallel to the x-axis and the other to the y-axis.
"""
import sys

def main():
    n = int(sys.stdin.readline())
    pts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    max_area2 = 0
    # For each point as the right-angle vertex
    for xi, yi in pts:
        # find vertical partner (same x)
        for xj, yj in pts:
            if xj == xi and yj != yi:
                # find horizontal partner (same y)
                for xk, yk in pts:
                    if yk == yi and xk != xi:
                        area2 = abs(yj - yi) * abs(xk - xi)
                        if area2 > max_area2:
                            max_area2 = area2
    print(max_area2)

if __name__ == '__main__':
    main()
