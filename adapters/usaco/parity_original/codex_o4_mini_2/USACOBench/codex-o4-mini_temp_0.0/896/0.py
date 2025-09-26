#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    mountains = []
    idx = 1
    for _ in range(N):
        x = int(data[idx]); y = int(data[idx+1])
        idx += 2
        # Compute interval on x-axis covered by the mountain
        L = x - y
        R = x + y
        mountains.append((L, R))
    # Sort by left endpoint asc, and right endpoint desc
    mountains.sort(key=lambda interval: (interval[0], -interval[1]))
    count = 0
    maxR = -10**18
    # Sweep and count visible mountains
    for L, R in mountains:
        if R > maxR:
            count += 1
            maxR = R
    print(count)

if __name__ == "__main__":
    main()
