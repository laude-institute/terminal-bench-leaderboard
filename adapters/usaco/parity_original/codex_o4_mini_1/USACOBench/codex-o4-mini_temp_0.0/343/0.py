#!/usr/bin/env python3
"""
Solution to nocow problem.
Reads missing cow adjective combinations and finds the K-th existing combination.
"""
import sys

def main():
    data = sys.stdin.read().split()
    # Read N and K
    N = int(data[0])
    K = int(data[1])
    # Parse missing combinations
    missing = []
    idx = 2
    for _ in range(N):
        # Skip the fixed tokens: 'Farmer John has no'
        idx += 4
        # Read adjectives until 'cow.' token
        combo = []
        while data[idx] != 'cow.':
            combo.append(data[idx])
            idx += 1
        idx += 1  # skip 'cow.'
        missing.append(combo)

    # Number of adjective positions
    M = len(missing[0])
    # Collect possible values per position
    possible = [set() for _ in range(M)]
    for combo in missing:
        for j, word in enumerate(combo):
            possible[j].add(word)
    # Sort values lexicographically
    sorted_vals = [sorted(lst) for lst in possible]

    # Build trie of missing combos for prefix counts
    class Node:
        def __init__(self):
            self.count = 0
            self.children = {}

    root = Node()
    for combo in missing:
        node = root
        node.count += 1
        for w in combo:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
            node.count += 1

    # Precompute suffix product of remaining positions
    suffix = [1] * M
    prod = 1
    for j in range(M - 1, -1, -1):
        suffix[j] = prod
        prod *= len(sorted_vals[j])

    # Find K-th existing combination
    result = []
    node = root
    k = K
    for j in range(M):
        for w in sorted_vals[j]:
            total = suffix[j]
            # Count missing combos under this prefix
            miss = node.children[w].count if node and w in node.children else 0
            avail = total - miss
            if k <= avail:
                result.append(w)
                node = node.children.get(w) if node else None
                break
            k -= avail

    # Output result
    sys.stdout.write(" ".join(result))

if __name__ == '__main__':
    main()
