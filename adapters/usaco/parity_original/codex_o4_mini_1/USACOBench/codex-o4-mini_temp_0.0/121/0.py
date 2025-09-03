#!/usr/bin/env python3
"""
Reads a binary number N from stdin, computes 17*N, and prints the result in binary.
"""
import sys

def main():
    # Read binary input, strip whitespace
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n_str = data[0]

    # Convert binary string to integer, multiply by 17, convert back to binary
    try:
        n = int(n_str, 2)
    except ValueError:
        # Invalid input
        return
    result = n * 17
    # Print binary representation without '0b' prefix
    print(bin(result)[2:])

if __name__ == '__main__':
    main()
