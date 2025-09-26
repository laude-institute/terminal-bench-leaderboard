#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    max_a = max(a)
    # s must satisfy no pile has >= 2*s stones: s > max_a//2
    start = max_a // 2 + 1
    # build frequency array
    freq = [0] * (max_a + 2)
    for v in a:
        freq[v] += 1
    # build suffix sums: count of piles with size >= s
    suffix = [0] * (max_a + 3)
    for s in range(max_a, 0, -1):
        suffix[s] = freq[s] + suffix[s+1]
    # count winning first moves
    result = 0
    for s in range(start, max_a+1):
        c = suffix[s]
        # all floor(a_i/s) <= 1 holds by s > max_a//2
        # winning if number of piles with a_i >= s is odd
        if c & 1:
            result += c
    print(result)

if __name__ == '__main__':
    main()
