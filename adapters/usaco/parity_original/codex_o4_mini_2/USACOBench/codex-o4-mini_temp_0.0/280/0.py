#!/usr/bin/env python3
"""
Reads N and K, then K pairs of unfriendly cow positions.
Computes the minimal number of photos needed so that no unfriendly pair
appears together in any photo. Uses greedy interval covering on cuts.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    # Build intervals where a cut must be placed: (left, right)
    intervals = []
    for _ in range(K):
        a = int(next(it)); b = int(next(it))
        l = min(a, b)
        r = max(a, b)
        # A cut between l and r must be at some position in [l, r-1]
        intervals.append((l, r-1))
    # Sort intervals by their right endpoint for greedy covering
    intervals.sort(key=lambda x: x[1])
    cuts = 0
    last_cut = -1
    for l, r in intervals:
        # If the last cut does not cover this interval
        if last_cut < l:
            cuts += 1
            last_cut = r
    # Number of photos is one more than number of cuts
    result = cuts + 1
    print(result)

if __name__ == '__main__':
    main()
