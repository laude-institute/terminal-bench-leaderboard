#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    particles = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1]); idx += 2
        particles.append((x, y))
    # Sort by x ascending, then y ascending
    particles.sort()
    # Compute length of longest strictly decreasing subsequence of y
    # which equals minimum survivors
    tails = []  # will store negative y tails
    for _, y in particles:
        b = -y
        # find insertion point for strict increasing LIS
        i = bisect.bisect_left(tails, b)
        if i == len(tails):
            tails.append(b)
        else:
            tails[i] = b
    # Answer is number of chains needed = LIS length
    print(len(tails))

if __name__ == '__main__':
    main()
