#!/usr/bin/env python3
import sys

def area(rect):
    """Compute area of a rectangle (x1,y1,x2,y2)."""
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

def overlap(a, b):
    """Compute overlapping area between rectangles a and b."""
    # overlap width and height
    w = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    h = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    return w * h

def main():
    # Read input for two billboards and the truck
    b1 = list(map(int, sys.stdin.readline().split()))
    b2 = list(map(int, sys.stdin.readline().split()))
    t  = list(map(int, sys.stdin.readline().split()))

    # Total visible area = sum of billboard areas minus their overlaps with the truck
    visible = area(b1) - overlap(b1, t)
    visible += area(b2) - overlap(b2, t)

    print(visible)

if __name__ == '__main__':
    main()
