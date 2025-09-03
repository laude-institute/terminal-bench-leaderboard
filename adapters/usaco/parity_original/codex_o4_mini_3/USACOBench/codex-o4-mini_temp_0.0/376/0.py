#!/usr/bin/env python3
"""
Solution to USACO 'skidesign' problem.
Reads N hill elevations and adjusts them so that the difference
between highest and lowest is at most 17, minimizing cost.
Cost to change a hill by x units is x^2.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    hills = list(map(int, data[1:1+n]))
    min_cost = float('inf')
    # Try every possible interval [low, low+17]
    for low in range(0, 101 - 17):
        high = low + 17
        cost = 0
        for h in hills:
            if h < low:
                d = low - h
                cost += d * d
            elif h > high:
                d = h - high
                cost += d * d
        if cost < min_cost:
            min_cost = cost
    print(min_cost)

if __name__ == '__main__':
    main()
