#!/usr/bin/env python3
import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    flavors = []
    idx = 1
    for _ in range(n):
        # read 5 flavor IDs
        f = list(map(int, data[idx:idx+5]))
        idx += 5
        flavors.append(f)

    # count occurrences of each non-empty subset of flavors
    subset_counts = {}
    for f in flavors:
        f.sort()
        # generate all non-empty subsets
        for r in range(1, 6):
            for comb in combinations(f, r):
                subset_counts[comb] = subset_counts.get(comb, 0) + 1

    # inclusion-exclusion to count compatible pairs
    compatible = 0
    for comb, cnt in subset_counts.items():
        if cnt < 2:
            continue
        pairs = cnt * (cnt - 1) // 2
        if len(comb) % 2 == 1:
            compatible += pairs
        else:
            compatible -= pairs

    total_pairs = n * (n - 1) // 2
    incompatible = total_pairs - compatible
    print(incompatible)

if __name__ == '__main__':
    main()
