#!/usr/bin/env python3
import sys

def main():
    # Read input for mower and feed billboards
    x1_m, y1_m, x2_m, y2_m = map(int, sys.stdin.readline().split())
    x1_f, y1_f, x2_f, y2_f = map(int, sys.stdin.readline().split())

    # Dimensions of the mower billboard
    width_m = x2_m - x1_m
    height_m = y2_m - y1_m

    # Compute overlap rectangle coordinates
    x1_o = max(x1_m, x1_f)
    y1_o = max(y1_m, y1_f)
    x2_o = min(x2_m, x2_f)
    y2_o = min(y2_m, y2_f)

    # Check if there is no overlap
    if x1_o >= x2_o or y1_o >= y2_o:
        print(width_m * height_m)
        return

    # Overlap dimensions
    overlap_w = x2_o - x1_o
    overlap_h = y2_o - y1_o

    # Determine minimum tarp area
    # Case 1: overlap spans full height -> cover left or right
    if overlap_h == height_m:
        left_w = x1_o - x1_m
        right_w = x2_m - x2_o
        tarp_area = min(left_w, right_w) * height_m
    # Case 2: overlap spans full width -> cover top or bottom
    elif overlap_w == width_m:
        bottom_h = y1_o - y1_m
        top_h = y2_m - y2_o
        tarp_area = min(bottom_h, top_h) * width_m
    # Otherwise, tarp must cover entire billboard
    else:
        tarp_area = width_m * height_m

    print(tarp_area)

if __name__ == '__main__':
    main()
