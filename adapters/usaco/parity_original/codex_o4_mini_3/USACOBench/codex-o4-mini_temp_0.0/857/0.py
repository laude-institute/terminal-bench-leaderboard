#!/usr/bin/env python3
"""
Solution for bucket milk transfer problem.
"""
import sys

def main():
    # Read bucket sizes for both barns
    buckets1 = list(map(int, sys.stdin.readline().split()))
    buckets2 = list(map(int, sys.stdin.readline().split()))
    # Set to collect possible milk amounts in barn1 after 4 transfers
    results = set()

    def dfs(day, b1, b2, m1, m2):
        # Four moves: days 0..3
        if day == 4:
            results.add(m1)
            return
        # Even day: transfer from barn1 to barn2
        if day % 2 == 0:
            for i, sz in enumerate(b1):
                new_b1 = b1[:i] + b1[i+1:]
                new_b2 = b2 + [sz]
                dfs(day+1, new_b1, new_b2, m1 - sz, m2 + sz)
        # Odd day: transfer from barn2 to barn1
        else:
            for i, sz in enumerate(b2):
                new_b1 = b1 + [sz]
                new_b2 = b2[:i] + b2[i+1:]
                dfs(day+1, new_b1, new_b2, m1 + sz, m2 - sz)

    # Start with initial milk amounts
    dfs(0, buckets1, buckets2, 1000, 1000)
    # Output number of distinct outcomes
    print(len(results))

if __name__ == '__main__':
    main()
