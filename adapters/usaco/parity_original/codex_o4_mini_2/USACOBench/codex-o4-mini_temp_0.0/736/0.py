#!/usr/bin/env python3
"""
Reads genomes of spotty and plain cows and counts positions
where spotty and plain have no character in common.
"""
import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    # Next N strings are spotty genomes, following N are plain genomes
    spotty = data[2:2+N]
    plain = data[2+N:2+2*N]
    count = 0
    # For each position, check if sets are disjoint
    for i in range(M):
        sset = {genome[i] for genome in spotty}
        pset = {genome[i] for genome in plain}
        if sset.isdisjoint(pset):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
