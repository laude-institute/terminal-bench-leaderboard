#!/usr/bin/env python3
"""
Compute the minimum area of a rectangular tarp needed to cover the exposed
portion of the lawnmower billboard, given another billboard that may obscure it.
"""
import sys

def main():
    data = sys.stdin.read().split()
    tx1, ty1, tx2, ty2, fx1, fy1, fx2, fy2 = map(int, data)
    # Total area of the lawnmower billboard
    total_area = (tx2 - tx1) * (ty2 - ty1)
    # Compute overlap rectangle
    ix1 = max(tx1, fx1)
    iy1 = max(ty1, fy1)
    ix2 = min(tx2, fx2)
    iy2 = min(ty2, fy2)
    # No overlap
    if ix1 >= ix2 or iy1 >= iy2:
        print(total_area)
        return
    # Check if feed billboard spans full height of target
    if fy1 <= ty1 and fy2 >= ty2:
        left_exposed = fx1 > tx1
        right_exposed = fx2 < tx2
        # Fully covered
        if not left_exposed and not right_exposed:
            print(0)
        # Exposed only on left
        elif left_exposed and not right_exposed:
            print((fx1 - tx1) * (ty2 - ty1))
        # Exposed only on right
        elif right_exposed and not left_exposed:
            print((tx2 - fx2) * (ty2 - ty1))
        # Exposed on both sides
        else:
            print(total_area)
        return
    # Check if feed billboard spans full width of target
    if fx1 <= tx1 and fx2 >= tx2:
        bottom_exposed = fy1 > ty1
        top_exposed = fy2 < ty2
        # Fully covered
        if not bottom_exposed and not top_exposed:
            print(0)
        # Exposed only on bottom
        elif bottom_exposed and not top_exposed:
            print((tx2 - tx1) * (fy1 - ty1))
        # Exposed only on top
        elif top_exposed and not bottom_exposed:
            print((tx2 - tx1) * (ty2 - fy2))
        # Exposed on both top and bottom
        else:
            print(total_area)
        return
    # Overlap doesn't span fully: need full tarp
    print(total_area)

if __name__ == '__main__':
    main()
