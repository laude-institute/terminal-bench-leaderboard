#!/usr/bin/env python3
import sys

def neighbors(combo, N):
    """Yield all combos within 550.    
    for dx in range(-2, 3):
        i = (combo[0] - 1 + dx) % N + 1
        for dy in range(-2, 3):
            j = (combo[1] - 1 + dy) % N + 1
            for dz in range(-2, 3):
                k = (combo[2] - 1 + dz) % N + 1
                yield (i, j, k)

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    combo1 = list(map(int, data[1:4]))
    combo2 = list(map(int, data[4:7]))
    valid = set()
    for c in neighbors(combo1, N):
        valid.add(c)
    for c in neighbors(combo2, N):
        valid.add(c)
    print(len(valid))

if __name__ == "__main__":
    main()
