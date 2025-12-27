#!/usr/bin/env python3
"""
Solution to Farmer John record keeping problem.
"""
import sys

def main():
    # Read number of records
    n = int(sys.stdin.readline().strip())
    counts = {}
    # Process each group of three cow names
    for _ in range(n):
        names = sys.stdin.readline().split()
        # Sort names to get canonical group
        names.sort()
        key = tuple(names)
        counts[key] = counts.get(key, 0) + 1
    # Output the maximum occurrence count
    print(max(counts.values()))

if __name__ == "__main__":
    main()
