#!/usr/bin/env python3
"""
Reads genomes of N spotty and N plain cows and counts positions
where the sets of characters at that position are disjoint.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    spotty = [next(it).strip() for _ in range(n)]
    plain = [next(it).strip() for _ in range(n)]
    count = 0
    for i in range(m):
        s_chars = {cow[i] for cow in spotty}
        p_chars = {cow[i] for cow in plain}
        if s_chars.isdisjoint(p_chars):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
