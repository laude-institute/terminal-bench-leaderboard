#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    leaf_sets = []
    all_features = set()
    for _ in range(n):
        k = int(next(it))
        features = set()
        for _ in range(k):
            f = next(it)
            features.add(f)
            all_features.add(f)
        leaf_sets.append(features)
    # Check each pair of features for compatibility
    features_list = list(all_features)
    m = len(features_list)
    for i in range(m):
        for j in range(i+1, m):
            f1 = features_list[i]
            f2 = features_list[j]
            has_10 = has_01 = has_11 = False
            for s in leaf_sets:
                p1 = f1 in s
                p2 = f2 in s
                if p1 and p2:
                    has_11 = True
                elif p1 and not p2:
                    has_10 = True
                elif p2 and not p1:
                    has_01 = True
                # early break if incompatible pattern found
                if has_10 and has_01 and has_11:
                    print("no")
                    return
    print("yes")

if __name__ == '__main__':
    main()
