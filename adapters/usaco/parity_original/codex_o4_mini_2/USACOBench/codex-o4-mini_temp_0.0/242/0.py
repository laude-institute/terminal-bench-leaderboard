#!/usr/bin/env python3
"""
Cow Crossings

Count the number of cows whose straight-line crossing paths do not intersect any other.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    # Read (a, b) pairs
    pairs = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        pairs.append((a, b))
    # Sort by a-coordinate
    pairs.sort(key=lambda x: x[0])
    # Extract b-coordinates in sorted order
    b_vals = [b for _, b in pairs]
    # Prepare prefix max of previous b's and suffix min of next b's
    prefix_max = [0] * n
    suffix_min = [0] * n
    # Use infinities
    NEG_INF = -10**18
    POS_INF = 10**18
    # Compute prefix_max
    current_max = NEG_INF
    for i in range(n):
        prefix_max[i] = current_max
        if b_vals[i] > current_max:
            current_max = b_vals[i]
    # Compute suffix_min
    current_min = POS_INF
    for i in range(n-1, -1, -1):
        suffix_min[i] = current_min
        if b_vals[i] < current_min:
            current_min = b_vals[i]
    # Count safe cows
    safe_count = 0
    for i in range(n):
        if b_vals[i] > prefix_max[i] and b_vals[i] < suffix_min[i]:
            safe_count += 1
    # Output result
    print(safe_count)

if __name__ == '__main__':
    main()
