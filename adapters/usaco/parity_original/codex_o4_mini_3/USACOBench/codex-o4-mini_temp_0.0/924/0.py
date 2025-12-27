#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n = int(data.readline())
    probs = [0.0] * n
    for i in range(n):
        # input given as integer p_i * 1e6
        pi = int(data.readline())
        probs[i] = pi / 1_000_000.0

    left = 0
    prod = 1.0   # product of (1-p) in window
    ssum = 0.0   # sum of p/(1-p) in window
    best = 0.0

    for right in range(n):
        p = probs[right]
        one_minus = 1.0 - p
        prod *= one_minus
        ssum += p / one_minus

        # shrink window until sum < 1
        while left <= right and ssum >= 1.0:
            pl = probs[left]
            oml = 1.0 - pl
            prod /= oml
            ssum -= pl / oml
            left += 1

        # update best probability of exactly one acceptance
        curr = prod * ssum
        if curr > best:
            best = curr

    # output as integer floor(best * 1e6)
    result = int(best * 1_000_000.0)
    print(result)

if __name__ == '__main__':
    main()
