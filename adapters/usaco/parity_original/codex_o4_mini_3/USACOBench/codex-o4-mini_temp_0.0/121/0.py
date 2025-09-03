#!/usr/bin/env python3
"""
Reads a binary number N from input, computes 17*N, and prints the result in binary.
"""
import sys

def main():
    # Read binary input and strip whitespace
    binary_str = sys.stdin.readline().strip()
    if not binary_str:
        return
    # Convert to integer, multiply by 17
    value = int(binary_str, 2) * 17
    # Convert back to binary string and print
    print(bin(value)[2:])

if __name__ == "__main__":
    main()
