#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    maxA = max(a)
    # count frequency of each value
    cnt = [0] * (maxA + 1)
    for v in a:
        cnt[v] += 1
    # compute f[s] = sum floor(a_i / s)
    odd = [0] * (maxA + 1)
    for s in range(1, maxA + 1):
        tot = 0
        # sum over multiples of s
        for m in range(s, maxA + 1, s):
            if cnt[m]:
                tot += cnt[m] * (m // s)
        odd[s] = tot & 1
    # determine winning s: odd[s]==1 and no odd multiple > s
    win = [0] * (maxA + 1)
    for s in range(maxA, 0, -1):
        if odd[s]:
            has_odd = False
            for m in range(2*s, maxA + 1, s):
                if odd[m]:
                    has_odd = True
                    break
            if not has_odd:
                win[s] = 1
    # suffix count of piles with a_i >= s
    suff = [0] * (maxA + 2)
    for v in range(maxA, 0, -1):
        suff[v] = suff[v+1] + cnt[v]
    # sum ways
    ans = 0
    for s in range(1, maxA + 1):
        if win[s]:
            ans += suff[s]
    print(ans)

if __name__ == '__main__':
    main()
