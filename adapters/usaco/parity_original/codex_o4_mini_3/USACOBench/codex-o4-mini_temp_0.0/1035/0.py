#!/usr/bin/env python3
import sys

def can_place(cows, n, d):
    # cows: sorted list of existing positions
    # check existing min gap
    for i in range(1, len(cows)):
        if cows[i] - cows[i-1] < d:
            return False
    placed = 0
    # before first cow
    if cows:
        placed += (cows[0] - 1) // d
    else:
        # no existing cows: we can place two anywhere
        return True
    # between cows
    for i in range(1, len(cows)):
        gap = cows[i] - cows[i-1]
        placed += max(0, gap // d - 1)
    # after last cow
    placed += (n - cows[-1]) // d
    return placed >= 2

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]
    cows = [i+1 for i, ch in enumerate(s) if ch == '1']
    # edge: no existing cows
    if not cows:
        print(n-1)
        return
    low, high = 1, n-1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(cows, n, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == '__main__':
    main()
