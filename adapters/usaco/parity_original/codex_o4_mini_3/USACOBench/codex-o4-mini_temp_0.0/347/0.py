#!/usr/bin/env python3
"""
Line of Sight: count pairs of cows with unobstructed view past a circular silo.
"""
import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    R = float(next(it))
    events = []  # (angle, type) type: +1=start, -1=end
    TWO_PI = 2.0 * math.pi
    for _ in range(N):
        x = float(next(it)); y = float(next(it))
        # polar angle of cow
        theta = math.atan2(y, x)
        if theta < 0:
            theta += TWO_PI
        # half-width of tangent-line angles
        d = math.hypot(x, y)
        beta = math.acos(R / d)
        start = theta - beta
        end = theta + beta
        # normalize interval to [0, 2pi)
        if start < 0:
            # wraps below zero
            events.append((start + TWO_PI, 1))
            events.append((TWO_PI, -1))
            events.append((0.0, 1))
            events.append((end, -1))
        elif end >= TWO_PI:
            # wraps above 2pi
            events.append((start, 1))
            events.append((TWO_PI, -1))
            events.append((0.0, 1))
            events.append((end - TWO_PI, -1))
        else:
            events.append((start, 1))
            events.append((end, -1))
    # sweep line to count overlapping intervals
    events.sort(key=lambda x: (x[0], -x[1]))
    active = 0
    visible_pairs = 0
    for angle, typ in events:
        if typ == 1:
            # new interval starts, overlaps with all active
            visible_pairs += active
            active += 1
        else:
            active -= 1
    # output result
    print(visible_pairs)

if __name__ == '__main__':
    main()
