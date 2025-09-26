#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read the array values
    arr = [int(next(it)) for _ in range(n)]
    # Pair each value with its original index
    pairs = [(val, idx) for idx, val in enumerate(arr)]
    # Sort by value, then by original index to maintain stability
    pairs.sort(key=lambda x: (x[0], x[1]))
    # Compute the maximum leftward shift
    max_shift = 0
    for new_idx, (_, orig_idx) in enumerate(pairs):
        shift = orig_idx - new_idx
        if shift > max_shift:
            max_shift = shift
    # Number of 'moo' prints is shifts + 1 (including final check)
    print(max_shift + 1)

if __name__ == '__main__':
    main()
