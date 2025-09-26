#!/usr/bin/env python3
import sys

def main():
    # Read N and K
    N, K = map(int, sys.stdin.readline().split())
    missing = []
    # Parse missing cows
    for _ in range(N):
        words = sys.stdin.readline().split()
        # adjectives are from index 4 up to before 'cow.'
        missing.append(tuple(words[4:-1]))
    M = len(missing[0])
    # Collect possible adjectives per position
    options = [set() for _ in range(M)]
    for cow in missing:
        for i in range(M):
            options[i].add(cow[i])
    # Sort options for lex order
    opts = [sorted(s) for s in options]
    # Precompute suffix products
    suffix_prod = [1] * (M + 1)
    for i in range(M - 1, -1, -1):
        suffix_prod[i] = suffix_prod[i + 1] * len(opts[i])
    rem_missing = missing
    result = []
    k = K
    # Build K-th valid cow
    for i in range(M):
        for adj in opts[i]:
            # Count missing cows under this prefix
            cnt_missing = sum(1 for cow in rem_missing
                              if cow[:i] == tuple(result) and cow[i] == adj)
            total = suffix_prod[i + 1]
            valid = total - cnt_missing
            if k <= valid:
                result.append(adj)
                # Filter missing to this prefix
                rem_missing = [cow for cow in rem_missing
                               if cow[:i+1] == tuple(result)]
                break
            k -= valid
    # Output result
    print(' '.join(result))

if __name__ == '__main__':
    main()
