#!/usr/bin/env python3
"""
Computes the maximum number of "yes" answers Elsie could receive before
distinguishing the correct animal. Based on finding the largest overlap
of characteristics between any two animals, then adding one.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    animals = []
    for _ in range(N):
        parts = input().strip().split()
        # parts[0] is name, parts[1] is count, rest are characteristics
        chars = set(parts[2:])
        animals.append(chars)

    max_common = 0
    # Compare each pair to find maximum shared characteristics
    for i in range(N):
        for j in range(i + 1, N):
            common = len(animals[i] & animals[j])
            if common > max_common:
                max_common = common

    # Elsie can get max_common shared yes answers plus one distinguishing yes
    print(max_common + 1)

if __name__ == '__main__':
    main()
