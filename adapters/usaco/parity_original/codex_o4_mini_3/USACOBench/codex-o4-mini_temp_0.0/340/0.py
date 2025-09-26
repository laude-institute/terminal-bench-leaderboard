#!/usr/bin/env python3
"""
Solution to Combination Lock problem (USACO 2013 Bronze 'combo').
Computes number of valid lock settings close to either of two combinations.
"""
def close_positions(c, N):
    # Return all positions within 2 of c on a circular dial 1..N
    positions = []
    for delta in (-2, -1, 0, 1, 2):
        pos = (c - 1 + delta) % N + 1
        positions.append(pos)
    return positions

def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    combo1 = list(map(int, data[1:4]))
    combo2 = list(map(int, data[4:7]))
    valid = set()
    # Generate all close settings for both combinations
    for combo in (combo1, combo2):
        for i in close_positions(combo[0], N):
            for j in close_positions(combo[1], N):
                for k in close_positions(combo[2], N):
                    valid.add((i, j, k))
    # Output the number of distinct valid settings
    print(len(valid))

if __name__ == "__main__":
    main()
