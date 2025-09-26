#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    n_line = data.readline().strip()
    if not n_line:
        return
    n = int(n_line)
    cows = []  # list of [output, count]
    for _ in range(n):
        x, y = map(int, data.readline().split())
        cows.append([y, x])
    # sort by milk output
    cows.sort(key=lambda t: t[0])
    l, r = 0, len(cows) - 1
    ans = 0
    # two-pointer pairing: smallest with largest
    while l <= r:
        # same group: pair internally
        if l == r:
            # there must be an even number of cows here
            if cows[l][1] >= 2:
                ans = max(ans, cows[l][0] * 2)
            break
        # number of pairs we can form between group l and r
        take = min(cows[l][1], cows[r][1])
        # update maximum pair sum
        ans = max(ans, cows[l][0] + cows[r][0])
        # decrement counts
        cows[l][1] -= take
        cows[r][1] -= take
        # move pointers if a group is exhausted
        if cows[l][1] == 0:
            l += 1
        if cows[r][1] == 0:
            r -= 1
    # output the minimum time needed
    print(ans)

if __name__ == '__main__':
    main()
