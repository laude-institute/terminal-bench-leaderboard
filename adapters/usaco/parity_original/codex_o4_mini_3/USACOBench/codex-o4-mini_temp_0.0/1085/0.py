#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    b = list(map(int, data[1+n:1+2*n]))
    a.sort()
    b.sort()
    size = 1 << n
    dp = [0] * size
    dp[0] = 1
    for mask in range(size):
        ways = dp[mask]
        if ways == 0:
            continue
        k = mask.bit_count()
        if k >= n:
            continue
        limit = b[k]
        for i in range(n):
            if not (mask >> i) & 1 and a[i] <= limit:
                dp[mask | (1 << i)] += ways
    print(dp[size - 1])

if __name__ == '__main__':
    main()
