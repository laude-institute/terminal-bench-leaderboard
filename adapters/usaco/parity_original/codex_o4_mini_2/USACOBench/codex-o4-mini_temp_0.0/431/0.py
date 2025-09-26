#!/usr/bin/env python3

import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for _ in range(N):
        x, b = input().split()
        x = int(x)
        cows.append((x, b))
    # sort cows by position
    cows.sort(key=lambda c: c[0])
    xs = [c[0] for c in cows]
    bs = [c[1] for c in cows]

    # find max interval with equal G and H
    prefix = 0
    first_occurrence = {0: 0}
    maxlen = 0
    for j in range(1, N+1):
        prefix += 1 if bs[j-1] == 'G' else -1
        if prefix in first_occurrence:
            i = first_occurrence[prefix]
            length = xs[j-1] - xs[i]
            if length > maxlen:
                maxlen = length
        else:
            first_occurrence[prefix] = j

    # find max homogenous segment (only one breed)
    i = 0
    while i < N:
        j = i
        while j + 1 < N and bs[j+1] == bs[i]:
            j += 1
        length = xs[j] - xs[i]
        if length > maxlen:
            maxlen = length
        i = j + 1

    print(maxlen)

if __name__ == '__main__':
    main()
