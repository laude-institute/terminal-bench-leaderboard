#!/usr/bin/env python3
"""
0.py - Solution to the Fair Photography problem
"""
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    cows = []
    idx = 1
    for _ in range(N):
        x = int(data[idx]); b = data[idx+1]; idx += 2
        cows.append((x, b))
    # sort by position
    cows.sort(key=lambda cb: cb[0])
    pos = [c[0] for c in cows]
    breed = [c[1] for c in cows]

    # 1) max span of single-breed runs
    max_size = 0
    start = 0
    for i in range(1, N):
        if breed[i] != breed[i-1]:
            size = pos[i-1] - pos[start]
            if size > max_size:
                max_size = size
            start = i
    # tail run
    size = pos[N-1] - pos[start]
    if size > max_size:
        max_size = size

    # 2) max span of equal G/H segments (prefix-sum technique)
    prefix_map = {0: -1}
    s = 0
    for i in range(N):
        s += 1 if breed[i] == 'G' else -1
        if s in prefix_map:
            j = prefix_map[s]
            start_idx = j + 1
            size = pos[i] - pos[start_idx]
            if size > max_size:
                max_size = size
        else:
            prefix_map[s] = i

    # output result
    print(max_size)

if __name__ == '__main__':
    main()
