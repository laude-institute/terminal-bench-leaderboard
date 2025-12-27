#!/usr/bin/env python3
"""
Maximize number of TV programs recorded on two tuners.
Sort programs by end time and greedily assign to available tuner.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    intervals = []
    for _ in range(n):
        s = int(next(it))
        e = int(next(it))
        intervals.append((e, s))
    # Sort by end time
    intervals.sort()
    # Two tuners availability times
    avail = [0, 0]
    count = 0
    for e, s in intervals:
        # ensure avail sorted: avail[0] <= avail[1]
        if avail[0] > avail[1]:
            avail[0], avail[1] = avail[1], avail[0]
        # assign to the tuner that frees latest but is free by s
        if s >= avail[1]:
            avail[1] = e
            count += 1
        elif s >= avail[0]:
            avail[0] = e
            count += 1
    print(count)

if __name__ == '__main__':
    main()
