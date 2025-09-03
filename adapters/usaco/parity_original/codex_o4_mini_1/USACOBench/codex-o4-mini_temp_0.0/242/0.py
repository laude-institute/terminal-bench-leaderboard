#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pairs = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        pairs.append((a, b))
    # Sort by starting x-coordinate
    pairs.sort(key=lambda x: x[0])
    # Extract ending y=1 coordinates
    b_list = [b for _, b in pairs]
    # Compute prefix maximum of b's
    prefix_max = [0] * n
    curr_max = -10**18
    for i in range(n):
        prefix_max[i] = curr_max
        if b_list[i] > curr_max:
            curr_max = b_list[i]
    # Compute suffix minimum of b's
    suffix_min = [0] * n
    curr_min = 10**18
    for i in range(n - 1, -1, -1):
        suffix_min[i] = curr_min
        if b_list[i] < curr_min:
            curr_min = b_list[i]
    # Count cows that have no crossings
    safe = 0
    for i in range(n):
        if b_list[i] > prefix_max[i] and b_list[i] < suffix_min[i]:
            safe += 1
    print(safe)

if __name__ == "__main__":
    main()
