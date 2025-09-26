#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    deg = [0] * (n + 1)
    idx = 1
    for _ in range(n - 1):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        deg[a] += 1
        deg[b] += 1
    # Calculate replication days
    rep_days = 0
    for node in range(1, n+1):
        # children count: for root (1), all neighbors; else deg-1
        if node == 1:
            children = deg[node]
        else:
            children = deg[node] - 1
        # days to replicate until cows >= children+1; equals ceil(log2(children+1))
        # which is bit_length of children
        rep_days += children.bit_length()
    # Each edge movement takes one day, total n-1 moves
    total_days = rep_days + (n - 1)
    print(total_days)

if __name__ == '__main__':
    main()
