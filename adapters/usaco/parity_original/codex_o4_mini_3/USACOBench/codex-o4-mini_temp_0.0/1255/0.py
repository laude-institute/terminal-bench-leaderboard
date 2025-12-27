#!/usr/bin/env python3
"""
Solution for the circular barn cow removal game.
Determine the winner based on the first room's cow count.
Lose positions are exactly those where a_1 % 6 == 4.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    res = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        # Read the first room count; skip the rest
        a1 = int(data[idx]); idx += 1
        idx += n - 1
        # Losing if a1 % 6 == 4
        if a1 % 6 == 4:
            res.append("Farmer Nhoj")
        else:
            res.append("Farmer John")
    sys.stdout.write("\n".join(res))

if __name__ == '__main__':
    main()
