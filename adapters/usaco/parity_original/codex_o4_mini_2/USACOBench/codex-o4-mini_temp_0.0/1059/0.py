#!/usr/bin/env python3
import sys

def main():
    # Read seven integers from standard input
    nums = list(map(int, sys.stdin.read().split()))
    # Sort the values to identify A, B and the total sum
    nums.sort()
    A = nums[0]
    B = nums[1]
    total = nums[-1]
    # Compute C from the total sum
    C = total - A - B
    # Output A, B, and C
    print(A, B, C)

if __name__ == "__main__":
    main()
