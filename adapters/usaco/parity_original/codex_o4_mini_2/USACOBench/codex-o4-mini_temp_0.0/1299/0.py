#!/usr/bin/env python3
"""
Compute total haybales Bessie eats in first T days.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n, t = map(int, data[:2])
    entries = data[2:]
    supply = 0
    eaten = 0
    prev_day = 1
    # Process each delivery
    for i in range(0, 2*n, 2):
        d = int(entries[i])
        b = int(entries[i+1])
        # Days between previous day and today (before today's dinner)
        days = d - prev_day
        # Eat at most one per day, limited by supply
        eat = min(supply, days)
        eaten += eat
        supply -= eat
        # Add today's delivery before dinner
        supply += b
        prev_day = d
    # After last delivery, eat until day T
    days = t - prev_day + 1
    eaten += min(supply, days)
    # Output result
    print(eaten)

if __name__ == '__main__':
    main()
