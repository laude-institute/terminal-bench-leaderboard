#!/usr/bin/env python3
"""
Reads seven integers representing A, B, C, A+B, B+C, C+A, A+B+C (in unknown order)
and recovers A, B, C (A <= B <= C).
"""
import sys

def main():
    nums = list(map(int, sys.stdin.read().split()))
    nums.sort()
    # The largest number is A+B+C
    total = nums[-1]
    # The smallest two are A and B
    a = nums[0]
    b = nums[1]
    # Recover C
    c = total - a - b
    print(a, b, c)

if __name__ == "__main__":
    main()
