#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    sizes = [int(next(it)) for _ in range(N)]
    sizes.sort()
    max_display = 0
    left = 0
    # sliding window to find longest range with size difference <= K
    for right in range(N):
        # shrink window if difference exceeds K
        while sizes[right] - sizes[left] > K:
            left += 1
        # update maximum window size
        current_size = right - left + 1
        if current_size > max_display:
            max_display = current_size
    print(max_display)

if __name__ == '__main__':
    main()
