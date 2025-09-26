#!/usr/bin/env python3
"""
Compute minimum years Bessie needs to visit all ancestors and return,
using at most K portal jumps around Ox years.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    # Read ancestor years ago
    X = [int(next(it)) for _ in range(N)]
    # Map each ancestor to a 12-year bin (Ox years at boundaries)
    bins = set((x - 1) // 12 for x in X)
    b = sorted(bins)
    M = len(b)
    # If we have at most K segments, each bin can be its own group
    if K >= M:
        # Each group costs 12 years
        print(12 * M)
        return
    # Compute gaps between consecutive bins (number of empty bins)
    gaps = [b[i+1] - b[i] - 1 for i in range(M - 1)]
    # To minimize coverage, remove the largest K-1 gaps
    gaps.sort(reverse=True)
    saved = sum(gaps[:K-1])
    # Total bins covered is span minus saved gaps
    total_bins = (b[-1] - b[0] + 1) - saved
    # Convert bin count back to years
    print(12 * total_bins)

if __name__ == '__main__':
    main()
