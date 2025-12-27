#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    x = int(data[1])
    h = list(map(int, data[2:2+n]))

    # Convert heights to +1/-1 based on threshold x
    b = [1 if hi >= x else -1 for hi in h]

    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + b[i-1]

    # Coordinate compression of prefix sums
    all_vals = sorted(set(prefix))
    comp = {v: i+1 for i, v in enumerate(all_vals)}  # ranks start at 1

    # Fenwick Tree for counting
    size = len(all_vals)
    bit = [0] * (size + 1)

    def bit_update(i):
        while i <= size:
            bit[i] += 1
            i += i & -i

    def bit_query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Count subarrays with positive sum
    result = 0
    # Initialize with prefix[0]
    bit_update(comp[prefix[0]])

    for i in range(1, n + 1):
        r = comp[prefix[i]]
        # count previous prefix sums < current
        result += bit_query(r - 1)
        bit_update(r)

    # Output result
    print(result)

if __name__ == '__main__':
    main()
