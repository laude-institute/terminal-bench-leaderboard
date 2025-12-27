#!/usr/bin/env python3
"""
Reads seven numbers representing A, B, C, A+B, B+C, C+A, A+B+C in any order
and recovers the original A, B, C.
"""
import sys

def main():
    # Read seven integers
    nums = list(map(int, sys.stdin.read().split()))
    # Sort numbers: smallest are A and B, largest is A+B+C
    nums.sort()
    A = nums[0]
    B = nums[1]
    total = nums[-1]
    # Recover C
    C = total - A - B
    # Output A, B, C
    print(A, B, C)

if __name__ == "__main__":
    main()
