#!/usr/bin/env python3
"""
Count the number of pairs of cows that are not compatible.
Two cows are compatible if they share at least one ice cream flavor.
"""
import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    n = int(input())
    # counts of cows having each subset of flavors
    subset_counts = {}
    for _ in range(n):
        flavors = list(map(int, input().split()))
        flavors.sort()
        # generate all non-empty subsets
        for k in range(1, 6):
            for comb in combinations(flavors, k):
                subset_counts[comb] = subset_counts.get(comb, 0) + 1
    # inclusion-exclusion to count pairs with >=1 common flavor
    compatible_pairs = 0
    for comb, count in subset_counts.items():
        if count < 2:
            continue
        pairs = count * (count - 1) // 2
        # add if odd-sized subset, subtract if even-sized
        if len(comb) % 2 == 1:
            compatible_pairs += pairs
        else:
            compatible_pairs -= pairs
    total_pairs = n * (n - 1) // 2
    # pairs not compatible = total - compatible
    print(total_pairs - compatible_pairs)

if __name__ == '__main__':
    main()
