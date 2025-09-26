#!/usr/bin/env python3
"""
Reads a sequence of cow heights after one cow has moved,
and computes the minimum number of swaps needed to sort them.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    # Pair each value with its original index
    arr_pos = [(val, idx) for idx, val in enumerate(arr)]
    # Sort by value to know target positions
    arr_pos.sort(key=lambda x: x[0])
    visited = [False] * n
    swaps = 0
    # Find cycles in the permutation
    for i in range(n):
        if visited[i] or arr_pos[i][1] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1
        if cycle_size > 0:
            swaps += cycle_size - 1
    # Output result
    print(swaps)

if __name__ == '__main__':
    main()
