#!/usr/bin/env python3
"""
Count pairs of cows with no common ice cream flavors.
Use inclusion-exclusion on subsets of favorites.
"""
import sys

def main():
    data = sys.stdin
    n = int(data.readline())
    counts = {}
    # Count occurrences of each non-empty subset of flavors
    for _ in range(n):
        flavors = list(map(int, data.readline().split()))
        flavors.sort()
        # Iterate through all non-empty subsets via bitmask
        for mask in range(1, 1 << 5):
            subset = []
            for i in range(5):
                if mask & (1 << i):
                    subset.append(flavors[i])
            key = tuple(subset)
            counts[key] = counts.get(key, 0) + 1

    # Inclusion-exclusion to count pairs with at least one common flavor
    pairs_with_common = 0
    for key, cnt in counts.items():
        if cnt < 2:
            continue
        pair_count = cnt * (cnt - 1) // 2
        # Add for odd-size subsets, subtract for even-size
        if len(key) % 2 == 1:
            pairs_with_common += pair_count
        else:
            pairs_with_common -= pair_count

    total_pairs = n * (n - 1) // 2
    # Pairs with no common flavor = total - with common
    print(total_pairs - pairs_with_common)

if __name__ == "__main__":
    main()
