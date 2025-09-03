#!/usr/bin/env python3
"""
Reads a binary number N, computes 17*N, and prints the result in binary.
"""
import sys

def main():
    # Read input binary string and strip whitespace
    s = sys.stdin.readline().strip()
    # Convert to integer, multiply by 17, then convert back to binary
    n = int(s, 2)
    result = n * 17
    # Print binary representation without '0b' prefix
    print(bin(result)[2:])

if __name__ == '__main__':
    main()
