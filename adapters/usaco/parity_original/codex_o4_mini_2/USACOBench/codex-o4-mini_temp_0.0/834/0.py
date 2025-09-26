#!/usr/bin/env python3
"""
Compute the number of 'moo' prints in Bessie's bubble sort simulation.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # Read array and keep original indices
    arr = [(int(data[i+1]), i) for i in range(n)]
    # Sort by value, break ties by original index (stable)
    arr.sort()
    # Map original index to sorted position
    sorted_pos = [0] * n
    for new_idx, (_, orig_idx) in enumerate(arr):
        sorted_pos[orig_idx] = new_idx
    # Compute max displacement to the left
    max_disp = 0
    for i in range(n):
        disp = i - sorted_pos[i]
        if disp > max_disp:
            max_disp = disp
    # Number of moos is max displacement + 1
    print(max_disp + 1)

if __name__ == '__main__':
    main()
