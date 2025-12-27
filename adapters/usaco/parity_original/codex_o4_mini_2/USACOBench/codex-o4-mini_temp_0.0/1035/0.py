#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    s = data[1]
    # positions of existing cows
    pos = [i for i, ch in enumerate(s) if ch == '1']
    # special case: no existing cows
    if not pos:
        # place at ends
        print(N - 1)
        return
    # compute original minimum spacing between existing cows
    INF = 10**18
    orig_min = INF
    for a, b in zip(pos, pos[1:]):
        orig_min = min(orig_min, b - a)
    # helper to check if we can place at least 2 cows with min distance D
    def can(D):
        cnt = 0
        # before first existing cow
        first = pos[0]
        cnt += first // D
        # between existing cows
        for a, b in zip(pos, pos[1:]):
            gap = b - a - D
            if gap >= 0:
                cnt += gap // D
        # after last existing cow
        tail = (N - 1) - pos[-1]
        cnt += tail // D
        return cnt >= 2
    # binary search maximum D
    lo = 1
    hi = orig_min if orig_min < INF else N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == '__main__':
    main()
