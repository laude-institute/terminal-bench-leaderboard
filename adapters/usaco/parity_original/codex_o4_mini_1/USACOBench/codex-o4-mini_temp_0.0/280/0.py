#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    N, K = map(int, data)
    intervals = []
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            a, b = b, a
        # allowed cut positions: [a, b-1]
        intervals.append((b-1, a))
    # sort by right endpoint
    intervals.sort()
    cuts = 0
    last_cut = 0
    for r, l in intervals:
        if last_cut < l:
            cuts += 1
            last_cut = r
    # segments count = cuts + 1
    print(cuts + 1)

if __name__ == "__main__":
    main()
