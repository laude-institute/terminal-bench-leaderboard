#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n = int(data.readline().strip())
    # Read (value, count) pairs
    freq = []  # list of [value, count]
    for _ in range(n):
        x, y = map(int, data.readline().split())
        freq.append([y, x])
    # Sort by milk output value
    freq.sort(key=lambda v: v[0])
    # Two-pointer pairing: smallest with largest
    left = 0
    right = len(freq) - 1
    ans = 0
    while left < right:
        low_val, low_cnt = freq[left]
        high_val, high_cnt = freq[right]
        # Update max time
        ans = max(ans, low_val + high_val)
        # Number of pairs to form between these groups
        m = min(low_cnt, high_cnt)
        # Decrement counts
        freq[left][1] -= m
        freq[right][1] -= m
        # Move pointers if group exhausted
        if freq[left][1] == 0:
            left += 1
        if freq[right][1] == 0:
            right -= 1
    # If one group remains, pair within itself
    if left == right and freq[left][1] > 0:
        # Remaining count must be even
        ans = max(ans, freq[left][0] * 2)
    # Print result
    print(ans)

if __name__ == '__main__':
    main()
