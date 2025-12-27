#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    idx = 1
    animals = []  # list of sets of characteristics
    for _ in range(n):
        name = data[idx]
        k = int(data[idx+1])
        idx += 2
        chars = set(data[idx:idx+k])
        idx += k
        animals.append(chars)
    max_common = 0
    # compute max intersection size over all pairs
    for i in range(n):
        for j in range(i+1, n):
            common = len(animals[i] & animals[j])
            if common > max_common:
                max_common = common
    # maximum yes answers is max_common + 1
    print(max_common + 1)

if __name__ == '__main__':
    main()
