#!/usr/bin/env python3
"""
Determine if a collection of cow feature sets can form a proper evolutionary tree.

For each feature, record the set of sub-population indices where it appears.
Check every pair of features to ensure their leaf sets are laminar: they must be disjoint
or one must be subset of the other. If any pair partially overlaps, output "no".
Otherwise, output "yes".
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Map feature -> bitmask of populations
    masks = {}
    for i in range(n):
        k = int(next(it))
        for _ in range(k):
            feat = next(it)
            masks[feat] = masks.get(feat, 0) | (1 << i)
    # Bitmask covering all populations
    all_mask = (1 << n) - 1
    feats = list(masks.keys())
    # Check laminar condition for each feature pair
    for i in range(len(feats)):
        for j in range(i + 1, len(feats)):
            x = masks[feats[i]]
            y = masks[feats[j]]
            common = x & y
            x_only = x & (all_mask ^ y)
            y_only = y & (all_mask ^ x)
            if common and x_only and y_only:
                print("no")
                return
    print("yes")

if __name__ == '__main__':
    main()
