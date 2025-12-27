#!/usr/bin/env python3
"""
Check if given sub-populations of cows with feature sets can form a proper evolutionary tree.
Each feature must arise exactly once, so feature sets must be laminar.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    feature_sets = {}  # feature -> set of population indices

    for idx in range(n):
        k = int(next(it))
        for _ in range(k):
            feat = next(it)
            feature_sets.setdefault(feat, set()).add(idx)

    # For each pair of features, their index sets must be disjoint or nested
    features = list(feature_sets.keys())
    m = len(features)
    for i in range(m):
        fi = features[i]
        si = feature_sets[fi]
        for j in range(i+1, m):
            fj = features[j]
            sj = feature_sets[fj]
            # Check intersection
            inter = si & sj
            if inter:
                # Must be nested
                if not (si <= sj or sj <= si):
                    print("no")
                    return
    print("yes")

if __name__ == '__main__':
    main()
