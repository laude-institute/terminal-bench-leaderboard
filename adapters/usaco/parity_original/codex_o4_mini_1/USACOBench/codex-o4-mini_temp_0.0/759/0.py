#!/usr/bin/env python3
import sys

def rect_area(x1, y1, x2, y2):
    """Compute area of rectangle given corners."""
    return max(0, x2 - x1) * max(0, y2 - y1)

def intersection_area(a, b):
    """Compute intersection area of two rectangles a and b.
    Each is a tuple (x1, y1, x2, y2)."""
    x1 = max(a[0], b[0])
    y1 = max(a[1], b[1])
    x2 = min(a[2], b[2])
    y2 = min(a[3], b[3])
    return rect_area(x1, y1, x2, y2)

def main():
    data = sys.stdin.read().strip().split()
    nums = list(map(int, data))
    # Unpack coordinates
    b1 = tuple(nums[0:4])
    b2 = tuple(nums[4:8])
    truck = tuple(nums[8:12])

    # Compute original billboard areas
    area1 = rect_area(*b1)
    area2 = rect_area(*b2)

    # Subtract overlap with truck
    vis1 = area1 - intersection_area(b1, truck)
    vis2 = area2 - intersection_area(b2, truck)

    # Total visible area
    print(vis1 + vis2)

if __name__ == '__main__':
    main()
