#!/usr/bin/env python3
"""
Solution to the Hay Bales problem:
Compute the minimum number of hay bales to move to equalize pile heights.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    total = sum(heights)
    avg = total // n
    # Minimum moves is sum of surpluses above average
    moves = sum(h - avg for h in heights if h > avg)
    print(moves)

if __name__ == '__main__':
    main()
