#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    # Create sorted copy
    sorted_heights = sorted(heights)
    # Count positions where heights differ
    mismatches = sum(1 for i in range(n) if heights[i] != sorted_heights[i])
    # Minimum swaps is mismatches - 1, but at least 0
    result = mismatches - 1 if mismatches > 0 else 0
    print(result)

if __name__ == "__main__":
    main()
