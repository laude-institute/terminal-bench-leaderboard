#!/usr/bin/env python3
"""
Solution to minimize the number of cows joining the lemonade line.
Sort tolerances descending and greedily count joins.
"""

import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    w = list(map(int, data[1:1+n]))
    # Sort tolerances descending
    w.sort(reverse=True)
    line_size = 0
    # Greedily add cows if their tolerance >= current line size
    for wi in w:
        if wi >= line_size:
            line_size += 1
        # else: cow leaves, do nothing
    # Print the minimum possible number of cows who join
    print(line_size)

if __name__ == "__main__":
    main()
