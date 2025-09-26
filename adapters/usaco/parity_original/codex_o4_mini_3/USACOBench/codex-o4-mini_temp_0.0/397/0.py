#!/usr/bin/env python3
"""
Solution to Auto-complete problem.
"""
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    W = int(data[0]); N = int(data[1])
    # Read dictionary words with original indices
    words = []
    idx = 2
    for i in range(W):
        words.append((data[idx], i+1))
        idx += 1
    # Sort by word
    words.sort(key=lambda x: x[0])
    sorted_words = [w for w, _ in words]
    sorted_indices = [i for _, i in words]
    out = []
    # Process queries
    for _ in range(N):
        K = int(data[idx]); prefix = data[idx+1]
        idx += 2
        # Find range of words with given prefix
        left = bisect.bisect_left(sorted_words, prefix)
        # Use character '{' (one after 'z') to get upper bound
        right = bisect.bisect_left(sorted_words, prefix + '{')
        # Check if there are enough completions
        if right - left < K:
            out.append('-1')
        else:
            out.append(str(sorted_indices[left + K - 1]))
    # Output results
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
