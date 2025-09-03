#!/usr/bin/env python3
"""
Reads N constraints of the form 'G p' or 'L p' and computes the minimum
number of lying statements by finding the hiding position x that maximizes
satisfied constraints. Prints the minimum number of lies.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    types = data[1::2]
    ps = list(map(int, data[2::2]))

    # Try each possible position x at the reported positions
    min_lies = n
    for x in ps:
        lies = 0
        # Count G p: lying if x < p; L p: lying if x > p
        for t, p in zip(types, ps):
            if t == 'G' and x < p:
                lies += 1
            elif t == 'L' and x > p:
                lies += 1
        if lies < min_lies:
            min_lies = lies

    # Output result
    print(min_lies)

if __name__ == '__main__':
    main()
