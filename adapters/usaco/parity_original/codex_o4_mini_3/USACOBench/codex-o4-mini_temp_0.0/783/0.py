#!/usr/bin/env python3
"""
Compute the minimum area of a rectangular tarp needed to cover the exposed
portion of the lawnmower billboard given overlap by the cow feed billboard.
"""
import sys

def main():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    # Dimensions of lawnmower billboard
    width = x2 - x1
    height = y2 - y1
    # Compute intersection
    ix1 = max(x1, x3)
    iy1 = max(y1, y3)
    ix2 = min(x2, x4)
    iy2 = min(y2, y4)
    iw = ix2 - ix1
    ih = iy2 - iy1
    # No overlap
    if iw <= 0 or ih <= 0:
        print(width * height)
        return
    # Overlap covers full width: horizontal strip
    if iw == width:
        # Remaining height above or below
        rem_h = max(iy1 - y1, y2 - iy2)
        print(rem_h * width)
        return
    # Overlap covers full height: vertical strip
    if ih == height:
        # Remaining width left or right
        rem_w = max(ix1 - x1, x2 - ix2)
        print(rem_w * height)
        return
    # Otherwise, tarp must cover entire billboard
    print(width * height)

if __name__ == "__main__":
    main()
