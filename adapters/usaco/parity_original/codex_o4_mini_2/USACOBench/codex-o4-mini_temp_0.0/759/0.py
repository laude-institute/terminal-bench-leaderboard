#!/usr/bin/env python3
"""
Compute the visible area of two billboards after being potentially obscured by a truck.
"""

def overlap_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """
    Compute the area of intersection between two axis-aligned rectangles.
    Each rectangle defined by lower-left (x1,y1) and upper-right (x2,y2).
    """
    # Determine overlap coordinates
    ox1 = max(ax1, bx1)
    oy1 = max(ay1, by1)
    ox2 = min(ax2, bx2)
    oy2 = min(ay2, by2)
    # Check if there is positive overlap
    if ox2 > ox1 and oy2 > oy1:
        return (ox2 - ox1) * (oy2 - oy1)
    return 0

def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    # First billboard
    x1, y1, x2, y2 = data[0:4]
    # Second billboard
    x3, y3, x4, y4 = data[4:8]
    # Truck
    tx1, ty1, tx2, ty2 = data[8:12]

    # Compute areas of billboards
    area1 = (x2 - x1) * (y2 - y1)
    area2 = (x4 - x3) * (y4 - y3)

    # Compute overlap with truck for each billboard
    overlap1 = overlap_area(x1, y1, x2, y2, tx1, ty1, tx2, ty2)
    overlap2 = overlap_area(x3, y3, x4, y4, tx1, ty1, tx2, ty2)

    # Visible area is total area minus obscured parts
    visible_total = (area1 - overlap1) + (area2 - overlap2)
    print(visible_total)

if __name__ == '__main__':
    main()
