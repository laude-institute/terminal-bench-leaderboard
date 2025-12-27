#!/usr/bin/env python3
import sys
import math
import bisect

def main():
    data = sys.stdin
    line = data.readline().split()
    if not line:
        return
    N, R = map(int, line)
    angles = []
    intervals = []
    for _ in range(N):
        x, y = map(int, data.readline().split())
        # compute angle of point
        theta = math.atan2(y, x)
        if theta < 0:
            theta += 2 * math.pi
        # distance and tangent half-angle
        d = math.hypot(x, y)
        phi = math.asin(R / d)
        a = theta - phi
        b = theta + phi
        # normalize interval to [0, 2*pi)
        if a < 0:
            intervals.append((a + 2 * math.pi, 2 * math.pi))
            intervals.append((0, b))
        elif b >= 2 * math.pi:
            intervals.append((a, 2 * math.pi))
            intervals.append((0, b - 2 * math.pi))
        else:
            intervals.append((a, b))
        angles.append(theta)
    # sort cow angles
    angles.sort()
    # count blocked ordered pairs
    blocked_ordered = 0
    for a, b in intervals:
        left = bisect.bisect_left(angles, a)
        right = bisect.bisect_right(angles, b)
        blocked_ordered += (right - left)
    # subtract self-counts (each cow counted once)
    blocked_ordered -= N
    # compute unordered blocked pairs
    blocked_pairs = blocked_ordered // 2
    total_pairs = N * (N - 1) // 2
    # visible pairs
    visible = total_pairs - blocked_pairs
    print(visible)

if __name__ == '__main__':
    main()
