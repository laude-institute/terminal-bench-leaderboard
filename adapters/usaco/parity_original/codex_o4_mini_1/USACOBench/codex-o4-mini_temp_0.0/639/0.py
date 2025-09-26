#!/usr/bin/env python3
"""
Solution to the diamond display problem:
Find the largest subset of diamond sizes where max - min <= K.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()
    max_count = 0
    left = 0
    # sliding window over sorted sizes
    for right in range(n):
        # shrink window until valid
        while sizes[right] - sizes[left] > k:
            left += 1
        # update best count
        curr_count = right - left + 1
        if curr_count > max_count:
            max_count = curr_count
    print(max_count)

if __name__ == "__main__":
    main()
