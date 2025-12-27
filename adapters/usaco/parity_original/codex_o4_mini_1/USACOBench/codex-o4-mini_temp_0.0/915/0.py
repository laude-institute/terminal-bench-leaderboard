#!/usr/bin/env python3
"""
Reads positions of three cows on a number line and computes
the minimum and maximum number of moves to make them occupy
three consecutive positions. A move consists of relocating an
endpoint cow to a position that is not currently an endpoint.
"""
import sys

def main():
    x, y, z = map(int, sys.stdin.readline().split())
    positions = sorted([x, y, z])
    x, y, z = positions
    # Compute gaps between consecutive cows
    gap1 = y - x
    gap2 = z - y

    # Minimum moves: special cases yield 0 or 1, else 2
    if gap1 == 1 and gap2 == 1:
        min_moves = 0
    elif gap1 == 2 or gap2 == 2:
        min_moves = 1
    else:
        min_moves = 2

    # Maximum moves: move endpoints inward one step each time
    max_moves = max(gap1, gap2) - 1

    print(min_moves)
    print(max_moves)

if __name__ == '__main__':
    main()
