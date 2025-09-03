#!/usr/bin/env python3
"""
Reads a list of cow heights after one cow has moved,
and computes the minimum number of swaps needed to
reorder cows from shortest to tallest.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    # Sorted heights for target order
    sorted_heights = sorted(heights)
    # Count positions where current differs from target
    mismatches = sum(1 for i in range(n) if heights[i] != sorted_heights[i])
    # If no mismatches, no swaps needed; else swaps = mismatches - 1
    result = mismatches - 1 if mismatches > 0 else 0
    print(result)

if __name__ == "__main__":
    main()
