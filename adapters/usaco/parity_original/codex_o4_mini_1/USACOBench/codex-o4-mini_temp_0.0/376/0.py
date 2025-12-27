#!/usr/bin/env python3
"""
Solution to 'skidesign' problem: adjust hill elevations
so that the max difference is at most 17, minimizing total cost.
Cost to change height by x units is x^2.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    hills = list(map(int, data[1:]))
    min_cost = float('inf')
    # Try all possible intervals [low, low+17]
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

if __name__ == "__main__":
    main()
