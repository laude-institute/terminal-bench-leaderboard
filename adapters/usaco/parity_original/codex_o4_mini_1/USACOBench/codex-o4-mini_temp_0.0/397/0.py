#!/usr/bin/env python3
"""
Auto-complete app: Given a dictionary and partial words,
find the Kth completion in alphabetical order.
"""
import sys
import bisect

def main():
    input = sys.stdin.readline
    W, N = map(int, input().split())
    # Read dictionary words with their original indices
    words = []  # list of tuples (word, original_index)
    for i in range(W):
        w = input().strip()
        words.append((w, i))
    # Sort words lexicographically by the word
    words.sort(key=lambda x: x[0])
    sorted_words = [w for w, _ in words]
    sorted_indices = [idx for _, idx in words]

    # Process queries
    for _ in range(N):
        line = input().split()
        K = int(line[0])
        prefix = line[1]
        # Find range of words starting with prefix
        low = bisect.bisect_left(sorted_words, prefix)
        # Use a character after 'z' to find the upper bound
        high = bisect.bisect_left(sorted_words, prefix + '{')
        # Check if there are at least K completions
        if K <= high - low:
            # Retrieve original index (convert to 1-based)
            orig_idx = sorted_indices[low + K - 1]
            print(orig_idx + 1)
        else:
            print(-1)

if __name__ == "__main__":
    main()
