#!/usr/bin/env python3
"""
Solution to 'The Lazy Cow' problem.
Reads N grass patches and distance K, finds maximum grass within any interval of length 2*K.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    patches = []  # list of (position, grass)
    for _ in range(N):
        g = int(next(it))
        x = int(next(it))
        patches.append((x, g))
    # Sort patches by position
    patches.sort(key=lambda t: t[0])
    left = 0
    curr_sum = 0
    max_sum = 0
    # Sliding window over positions with range 2*K
    for right in range(N):
        curr_sum += patches[right][1]
        # Shrink window from left if out of range
        while patches[right][0] - patches[left][0] > 2 * K:
            curr_sum -= patches[left][1]
            left += 1
        if curr_sum > max_sum:
            max_sum = curr_sum
    # Output result
    print(max_sum)

if __name__ == '__main__':
    main()
