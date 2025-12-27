#!/usr/bin/env python3
"""
Minimum photos to cover cows without unfriendly pairs in any photo.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    k = int(next(it))
    intervals = []
    for _ in range(k):
        a = int(next(it)); b = int(next(it))
        l = min(a, b)
        r = max(a, b) - 1
        if l <= r:
            intervals.append((l, r))
    # Greedy hitting of intervals by breakpoints
    intervals.sort(key=lambda x: x[1])
    breaks = 0
    last_break = 0
    for l, r in intervals:
        if last_break < l:
            breaks += 1
            last_break = r
    # Photos = breaks + 1
    print(breaks + 1)

if __name__ == '__main__':
    main()
