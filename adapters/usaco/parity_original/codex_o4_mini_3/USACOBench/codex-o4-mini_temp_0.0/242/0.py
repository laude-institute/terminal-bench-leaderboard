#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    cows = []  # list of (a, b)
    for _ in range(n):
        a = int(next(it)); b = int(next(it))
        cows.append((a, b))
    # Sort cows by starting x-coordinate a
    cows.sort(key=lambda x: x[0])
    bs = [b for _, b in cows]
    n = len(bs)
    # Compute prefix maximums of b
    prefix_max = [0] * n
    max_so_far = -10**18
    for i in range(n):
        prefix_max[i] = max_so_far
        if bs[i] > max_so_far:
            max_so_far = bs[i]
    # Compute suffix minimums of b
    suffix_min = [0] * n
    min_so_far = 10**18
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min_so_far
        if bs[i] < min_so_far:
            min_so_far = bs[i]
    # Count safe cows
    safe = 0
    for i in range(n):
        if prefix_max[i] < bs[i] and suffix_min[i] > bs[i]:
            safe += 1
    print(safe)

if __name__ == '__main__':
    main()
