#!/usr/bin/env python3

"""
Reads the ending date and time of Bessie's contest session,
calculates the minutes elapsed since 11/11/11 11:11,
and prints the elapsed minutes or -1 if the ending time is earlier.
"""

def main():
    # Read input: day, hour, minute
    D, H, M = map(int, input().split())

    # Contest start time: 11th day, 11:11
    # Convert both times to absolute minutes since an arbitrary epoch
    start_minutes = ((11 * 24) + 11) * 60 + 11
    end_minutes = ((D  * 24) + H) * 60 + M

    elapsed = end_minutes - start_minutes
    # If end time is before start, print -1
    if elapsed < 0:
        print(-1)
    else:
        print(elapsed)

if __name__ == '__main__':
    main()
