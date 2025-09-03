#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin
    first = data.readline().split()
    W, N = map(int, first)
    words = []
    for i in range(W):
        w = data.readline().strip()
        words.append((w, i+1))
    # Sort words lexicographically
    words.sort(key=lambda x: x[0])
    # Separate lists for binary search
    word_list = [w for w, _ in words]
    idx_list = [idx for _, idx in words]
    # Process queries
    for _ in range(N):
        parts = data.readline().split()
        k = int(parts[0])
        prefix = parts[1]
        # Find leftmost and rightmost bounds for prefix
        left = bisect.bisect_left(word_list, prefix)
        right = bisect.bisect_left(word_list, prefix + '{')
        # Check if there are at least k completions
        if right - left >= k:
            print(idx_list[left + k - 1])
        else:
            print(-1)

if __name__ == "__main__":
    main()
