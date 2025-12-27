#!/usr/bin/env python3
"""
Compute the total minutes Bessie spends in the contest.
Starts at 11/11 11:11. Output -1 if ending before start.
"""
import sys

def main():
    # Read end date and time
    data = sys.stdin.read().strip().split()
    if len(data) != 3:
        return
    D, H, M = map(int, data)

    # Compute absolute minutes since a fixed reference
    # Start: day 11, hour 11, minute 11
    start_minutes = (11 * 24 + 11) * 60 + 11
    # End: given D, H, M
    end_minutes = (D * 24 + H) * 60 + M

    # Calculate difference
    diff = end_minutes - start_minutes
    # Output result or -1 if negative
    print(diff if diff >= 0 else -1)

if __name__ == "__main__":
    main()
