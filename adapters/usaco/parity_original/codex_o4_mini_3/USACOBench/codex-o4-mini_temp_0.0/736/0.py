#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N, M = map(int, data[:2])
    spotty = data[2:2+N]
    plain = data[2+N:2+2*N]

    count = 0
    # Check each position for disjoint characters
    for i in range(M):
        s_chars = set(cow[i] for cow in spotty)
        p_chars = set(cow[i] for cow in plain)
        if s_chars.isdisjoint(p_chars):
            count += 1

    print(count)

if __name__ == '__main__':
    main()
