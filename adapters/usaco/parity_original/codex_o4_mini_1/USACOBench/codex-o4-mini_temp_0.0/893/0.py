#!/usr/bin/env python3
"""
Solution to 'guess the animal' problem.
Reads N animals with their characteristics, computes the maximum number
of shared characteristics between any two animals, and outputs that
maximum plus one (the worst-case number of 'yes' answers).
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    animals = []  # list of sets of characteristics
    for _ in range(N):
        parts = input().split()
        # parts[0] is animal name, parts[1] is count
        chars = set(parts[2:])
        animals.append(chars)

    max_common = 0
    # compare each pair of animals
    for i in range(N):
        for j in range(i + 1, N):
            common = len(animals[i] & animals[j])
            if common > max_common:
                max_common = common

    # worst-case yes answers is max_common + 1
    print(max_common + 1)

if __name__ == "__main__":
    main()
