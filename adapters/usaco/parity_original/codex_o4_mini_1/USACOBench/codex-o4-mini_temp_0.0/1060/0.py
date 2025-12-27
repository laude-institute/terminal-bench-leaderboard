#!/usr/bin/env python3
"""
Solution to count subarrays where an element equals the average.
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    petals = list(map(int, data[1:1+n]))
    # build prefix sums for O(1) range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + petals[i]

    count = 0
    # iterate all subarrays [i, j]
    for i in range(n):
        for j in range(i, n):
            total = prefix[j+1] - prefix[i]
            length = j - i + 1
            # check if average is an integer
            if total % length != 0:
                continue
            avg = total // length
            # check if any flower in subarray equals avg
            for k in range(i, j+1):
                if petals[k] == avg:
                    count += 1
                    break
    print(count)

if __name__ == '__main__':
    main()
