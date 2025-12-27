#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    patches = []
    for _ in range(N):
        g = int(next(it)); x = int(next(it))
        patches.append((x, g))
    patches.sort()
    left = 0
    current_sum = 0
    max_sum = 0
    twoK = 2 * K
    for right in range(N):
        current_sum += patches[right][1]
        while patches[right][0] - patches[left][0] > twoK:
            current_sum -= patches[left][1]
            left += 1
        if current_sum > max_sum:
            max_sum = current_sum
    sys.stdout.write(str(max_sum))

if __name__ == "__main__":
    main()
