#!/usr/bin/env python3
"""
Compute the number of times "moo" is printed by Bessie's bubble sort.
The bubble sort prints "moo" once per outer loop iteration,
which equals 1 plus the maximum leftward distance any element moves.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # Pair each element with its original index
    A = [(int(data[i+1]), i) for i in range(n)]
    # Stable sort by value then original index
    A.sort(key=lambda x: (x[0], x[1]))
    # Compute maximum leftward shift
    max_shift = 0
    for new_idx, (_, orig_idx) in enumerate(A):
        shift = orig_idx - new_idx
        if shift > max_shift:
            max_shift = shift
    # Number of moos is max_shift + 1
    print(max_shift + 1)

if __name__ == "__main__":
    main()
