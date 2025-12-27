#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cows = []
    idx = 1
    for _ in range(n):
        x = int(data[idx]); b = int(data[idx+1])
        cows.append((x, b))
        idx += 2

    # Sort cows by position
    cows.sort(key=lambda x: x[0])

    # Total distinct breeds
    total_breeds = len(set(b for _, b in cows))

    counts = {}
    unique = 0
    res = float('inf')
    left = 0

    # Sliding window over sorted cows
    for right in range(n):
        breed = cows[right][1]
        counts[breed] = counts.get(breed, 0) + 1
        if counts[breed] == 1:
            unique += 1

        # Shrink from left while covering all breeds
        while unique == total_breeds:
            width = cows[right][0] - cows[left][0]
            if width < res:
                res = width
            lb = cows[left][1]
            counts[lb] -= 1
            if counts[lb] == 0:
                unique -= 1
            left += 1

    # Output result
    print(res)

if __name__ == '__main__':
    main()
