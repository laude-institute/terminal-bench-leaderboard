#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    petals = list(map(int, data[1:1+n]))

    # Compute prefix sums for quick range sum queries
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + petals[i]

    count = 0
    # Iterate over all subarrays [i, j]
    for i in range(n):
        for j in range(i, n):
            total = prefix[j+1] - prefix[i]
            length = j - i + 1
            # Check if average is integer
            if total % length != 0:
                continue
            avg = total // length
            # Check if any flower in the subarray has petal count equal to average
            for k in range(i, j+1):
                if petals[k] == avg:
                    count += 1
                    break

    print(count)

if __name__ == '__main__':
    main()
