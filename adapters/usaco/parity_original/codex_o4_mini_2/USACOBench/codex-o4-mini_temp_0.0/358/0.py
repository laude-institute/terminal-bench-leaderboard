#!/usr/bin/env python3
"""
Records the most frequent group of three cows entering.
"""
def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    freq = {}
    for _ in range(n):
        # Read and sort the three cow names to form a canonical group key
        names = input().strip().split()
        names.sort()
        key = tuple(names)
        freq[key] = freq.get(key, 0) + 1
    # Print the maximum occurrence among all groups
    print(max(freq.values()) if freq else 0)

if __name__ == "__main__":
    main()
