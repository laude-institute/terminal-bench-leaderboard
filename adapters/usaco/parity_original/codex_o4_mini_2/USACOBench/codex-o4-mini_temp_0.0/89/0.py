#!/usr/bin/env python3
"""
Solution to Cow Lineup problem.
Find the minimum x-coordinate range covering all distinct breeds.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    cows = []  # list of (x, breed)
    for _ in range(n):
        x = int(next(it))
        b = int(next(it))
        cows.append((x, b))

    # Sort cows by position
    cows.sort(key=lambda cb: cb[0])

    # Total distinct breeds
    total_types = len({b for _, b in cows})

    counts = {}  # breed -> count in current window
    distinct = 0
    ans = float('inf')
    left = 0

    # Sliding window over sorted cows
    for right in range(n):
        breed = cows[right][1]
        counts[breed] = counts.get(breed, 0) + 1
        if counts[breed] == 1:
            distinct += 1

        # Try to shrink window when all breeds are included
        while distinct == total_types and left <= right:
            curr_cost = cows[right][0] - cows[left][0]
            if curr_cost < ans:
                ans = curr_cost
            left_breed = cows[left][1]
            counts[left_breed] -= 1
            if counts[left_breed] == 0:
                distinct -= 1
            left += 1

    # Output result
    print(ans)

if __name__ == '__main__':
    main()
