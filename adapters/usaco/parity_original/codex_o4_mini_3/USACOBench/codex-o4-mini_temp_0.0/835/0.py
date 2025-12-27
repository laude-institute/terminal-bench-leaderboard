#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    w = list(map(int, input().split()))
    w.sort()
    idx = 0
    for k in range(N + 1):
        # advance idx to first cow with w[idx] >= k
        while idx < N and w[idx] < k:
            idx += 1
        # if remaining cows <= k, they all inevitably join at most k
        if N - idx <= k:
            print(k)
            return

if __name__ == "__main__":
    main()
