#!/usr/bin/env python3
import sys

def main():
    # Read input values
    N, K = map(int, sys.stdin.readline().split())
    missing = []
    # Parse missing cow descriptions
    for _ in range(N):
        words = sys.stdin.readline().split()
        # adjectives are between 'no' and 'cow.'
        adjs = words[4:-1]
        missing.append(adjs)
    # Number of adjective positions
    M = len(missing[0])
    # Collect all possible adjectives per position
    values = [set() for _ in range(M)]
    for combo in missing:
        for i in range(M):
            values[i].add(combo[i])
    # Sort adjectives lexicographically
    for i in range(M):
        values[i] = sorted(values[i])
    # Precompute suffix product of sizes
    sizes = [len(values[i]) for i in range(M)]
    suffix = [1] * (M + 1)
    for i in range(M - 1, -1, -1):
        suffix[i] = sizes[i] * suffix[i + 1]
    # Build K-th valid combination
    result = []
    for i in range(M):
        for adj in values[i]:
            # Count total combinations for remaining positions
            total = suffix[i + 1]
            # Count how many missing combos share this prefix
            prefix = result + [adj]
            bad = sum(1 for combo in missing if combo[:i + 1] == prefix)
            cnt = total - bad
            if K > cnt:
                K -= cnt
            else:
                result.append(adj)
                break
    # Output the K-th cow description
    print(' '.join(result))

if __name__ == '__main__':
    main()
