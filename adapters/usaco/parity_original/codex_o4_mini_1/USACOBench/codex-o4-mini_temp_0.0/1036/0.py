#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sick = []
    healthy = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); s = int(data[idx+1])
        idx += 2
        if s == 1:
            sick.append(x)
        else:
            healthy.append(x)

    # If there are no healthy cows, one initial sick cow suffices
    if not healthy:
        print(1)
        return

    # Compute minimum distance between any sick and any healthy cow
    healthy.sort()
    dmin = float('inf')
    for x in sick:
        i = bisect.bisect_left(healthy, x)
        if i < len(healthy):
            dmin = min(dmin, abs(healthy[i] - x))
        if i > 0:
            dmin = min(dmin, abs(x - healthy[i-1]))

    # Maximum infection radius R is just below dmin
    R = dmin - 1

    # Group sick cows: a new initial if gap > R
    sick.sort()
    groups = 1
    for i in range(1, len(sick)):
        if sick[i] - sick[i-1] > R:
            groups += 1

    print(groups)

if __name__ == '__main__':
    main()
