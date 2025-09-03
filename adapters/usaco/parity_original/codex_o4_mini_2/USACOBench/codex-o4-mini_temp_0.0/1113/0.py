#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = list(map(int, it))
    maxA = max(a)
    # frequency of each pile size
    freq = [0] * (maxA + 2)
    for x in a:
        freq[x] += 1
    # P[s] = number of piles with size >= s
    P = [0] * (maxA + 2)
    P[maxA + 1] = 0
    for s in range(maxA, 0, -1):
        P[s] = freq[s] + P[s + 1]
    ans = 0
    # consider each possible first removal size s
    for s in range(1, maxA + 1):
        # number of piles Bessie can remove s stones from
        cnt = P[s]
        if cnt < 1:
            continue
        # if only one pile eligible, immediate loss
        if cnt == 1:
            continue
        # total capacities sum M = sum floor(a_i/s)
        M = 0
        # compute by summing P at multiples of s
        for t in range(s, maxA + 1, s):
            M += P[t]
        # max capacity Cmax = floor(maxA/s)
        cmax = maxA // s
        # count piles with capacity == Cmax
        low = cmax * s
        # piles with size >= low
        ge = P[low] if low <= maxA else 0
        # piles with size >= low+s
        ge_next = P[low + s] if low + s <= maxA else 0
        f = ge - ge_next
        # if unique max capacity, losing
        if f == 1:
            continue
        # else, winning if total moves odd
        if M & 1:
            ans += cnt
    print(ans)

if __name__ == '__main__':
    main()
