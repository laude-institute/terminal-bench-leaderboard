#!/usr/bin/env python3
"""
Compute minimum waiting time for Bessie's time-travel visits.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    times = [int(next(it)) for _ in range(N)]
    # Sort years ago ascending (closest first)
    times.sort()
    # Compute low and high Ox-year boundaries
    low = [t // 12 * 12 for t in times]
    high = [((t + 11) // 12) * 12 for t in times]
    # Base wait: one segment covering all
    base = high[-1] - low[0]
    # If only one portal jump allowed, no splits
    # segments = K-1 splits => max_splits = K-1
    max_splits = K - 1
    # Compute savings for each possible split
    # saving[i] = low[i+1] - high[i]
    savings = []
    for i in range(N - 1):
        savings.append(low[i+1] - high[i])
    # Sort savings descending
    savings.sort(reverse=True)
    # Sum best splits (only positive savings)
    total_saving = 0
    for i in range(min(max_splits, len(savings))):
        if savings[i] > 0:
            total_saving += savings[i]
        else:
            break
    # Resulting minimum wait
    result = base - total_saving
    print(result)

if __name__ == '__main__':
    main()
