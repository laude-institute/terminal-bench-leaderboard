#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    arr = [int(next(it)) for _ in range(N)]

    counts = {}
    max_breed = -1

    for i, breed in enumerate(arr):
        counts[breed] = counts.get(breed, 0) + 1
        if counts[breed] == 2 and breed > max_breed:
            max_breed = breed
        if i >= K:
            old = arr[i - K]
            counts[old] -= 1

    print(max_breed)

if __name__ == "__main__":
    main()
