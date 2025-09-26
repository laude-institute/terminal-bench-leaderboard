#!/usr/bin/env python3
"""
Solution for Hay Bales problem.
Reads N pile heights, computes average height, and sums surpluses.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    total = sum(heights)
    # original equal height per pile
    avg = total // n
    # count bales moved: sum of surpluses above avg
    moves = sum(h - avg for h in heights if h > avg)
    print(moves)

if __name__ == "__main__":
    main()
