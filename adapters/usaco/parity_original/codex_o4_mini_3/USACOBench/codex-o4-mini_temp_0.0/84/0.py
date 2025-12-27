#!/usr/bin/env python3
"""
USACO ctiming: compute minutes spent from 11/11 11:11 to given date/time.
"""
def main():
    # Read end date/time
    D, H, M = map(int, input().split())
    # Start date/time: 11th at 11:11
    start_day, start_hour, start_minute = 11, 11, 11
    # Compute difference in minutes
    diff = (D - start_day) * 24 * 60
    diff += (H - start_hour) * 60
    diff += (M - start_minute)
    # Output result or -1 if negative
    print(diff if diff >= 0 else -1)

if __name__ == "__main__":
    main()
