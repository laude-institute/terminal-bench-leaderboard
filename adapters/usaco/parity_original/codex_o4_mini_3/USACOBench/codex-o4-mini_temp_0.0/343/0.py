#!/usr/bin/env python3
"""
Solution to the 'nocow' problem.
Reads a list of missing cow adjective combinations,
then finds the Kth existing cow in lex order.
"""
import sys

def main():
    data = sys.stdin
    # Read N and K
    line = data.readline().split()
    N, K = int(line[0]), int(line[1])
    # Read missing cows
    missing = []
    for _ in range(N):
        tokens = data.readline().split()
        # adjectives are between 'no' and 'cow.'
        adjectives = tokens[4:-1]
        missing.append(tuple(adjectives))
    # Number of adjective positions
    M = len(missing[0]) if missing else 0
    # Gather possible adjectives per position
    adjs_sets = [set() for _ in range(M)]
    for cow in missing:
        for i, adj in enumerate(cow):
            adjs_sets[i].add(adj)
    # Sort adjectives for lex order
    adjs = [sorted(lst) for lst in adjs_sets]
    # Precompute product of remaining choices after each position
    rem_mult = [1] * M
    prod = 1
    for i in range(M-1, -1, -1):
        rem_mult[i] = prod
        prod *= len(adjs[i])

    # Helper to count missing cows with given prefix
    def count_missing(prefix):  # prefix is a tuple
        cnt = 0
        plen = len(prefix)
        for cow in missing:
            if cow[:plen] == prefix:
                cnt += 1
        return cnt

    # Find Kth existing cow
    result = []
    k = K
    for i in range(M):
        for adj in adjs[i]:
            prefix = tuple(result + [adj])
            total = rem_mult[i]
            miss = count_missing(prefix)
            avail = total - miss
            if k <= avail:
                result.append(adj)
                break
            k -= avail

    # Output the answer
    print(" ".join(result))

if __name__ == '__main__':
    main()
