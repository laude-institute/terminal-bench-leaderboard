#!/usr/bin/env python3
import sys

def main():
    # Read N and K
    N, K = map(int, sys.stdin.readline().split())
    # Read absent cow descriptions
    absent = []
    for _ in range(N):
        tokens = sys.stdin.readline().strip().split()
        # adjectives are between 'no' and 'cow.'
        adj = tokens[4:-1]
        absent.append(tuple(adj))
    # Number of adjective positions
    M = len(absent[0])
    # Collect possible adjectives per position
    alph = [set() for _ in range(M)]
    for t in absent:
        for i, w in enumerate(t):
            alph[i].add(w)
    # Sort each adjective list
    alph_list = [sorted(s) for s in alph]
    sizes = [len(lst) for lst in alph_list]
    # Precompute suffix products of sizes
    suffix = [1] * (M + 1)
    for i in range(M - 1, -1, -1):
        suffix[i] = sizes[i] * suffix[i + 1]
    # Count absent prefixes
    prefix_count = {}
    for t in absent:
        for i in range(1, M + 1):
            p = t[:i]
            prefix_count[p] = prefix_count.get(p, 0) + 1
    # Build the K-th valid cow description
    res = []
    prefix = ()
    remaining = K
    for i in range(M):
        for w in alph_list[i]:
            new_prefix = prefix + (w,)
            total = suffix[i + 1]
            absent_sub = prefix_count.get(new_prefix, 0)
            valid = total - absent_sub
            if remaining <= valid:
                res.append(w)
                prefix = new_prefix
                break
            remaining -= valid
    # Output result
    print(' '.join(res))

if __name__ == '__main__':
    main()
