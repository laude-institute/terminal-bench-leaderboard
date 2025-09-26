#!/usr/bin/env python3
import sys

def main():
    # Read input N
    N = int(sys.stdin.readline())
    # Function to count numbers <= x not divisible by 3 or 5
    def count_spoken(x):
        return x - x//3 - x//5 + x//15
    # Binary search for smallest x with count_spoken(x) >= N
    low, high = 1, 2 * N + 10
    while low < high:
        mid = (low + high) // 2
        if count_spoken(mid) >= N:
            high = mid
        else:
            low = mid + 1
    # Output the Nth spoken number
    print(low)

if __name__ == '__main__':
    main()
