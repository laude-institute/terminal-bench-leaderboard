#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, D = map(int, input().split())
    cows = [tuple(map(int, input().split())) for _ in range(N)]
    cows.sort(key=lambda t: t[0])
    xs = [cows[i][0] for i in range(N)]
    hs = [cows[i][1] for i in range(N)]
    left_ok = [False] * N
    right_ok = [False] * N
    dq = deque()
    # scan left to right for left crowding
    for i in range(N):
        x, h = xs[i], hs[i]
        while dq and x - xs[dq[0]] > D:
            dq.popleft()
        if dq and hs[dq[0]] >= 2 * h:
            left_ok[i] = True
        while dq and hs[dq[-1]] <= h:
            dq.pop()
        dq.append(i)
    # scan right to left via reversed coordinates
    xs_rev = [-x for x in reversed(xs)]
    hs_rev = list(reversed(hs))
    left_rev = [False] * N
    dq = deque()
    for i in range(N):
        x, h = xs_rev[i], hs_rev[i]
        while dq and x - xs_rev[dq[0]] > D:
            dq.popleft()
        if dq and hs_rev[dq[0]] >= 2 * h:
            left_rev[i] = True
        while dq and hs_rev[dq[-1]] <= h:
            dq.pop()
        dq.append(i)
    for i in range(N):
        if left_rev[N - 1 - i]:
            right_ok[i] = True
    result = sum(1 for i in range(N) if left_ok[i] and right_ok[i])
    print(result)

if __name__ == "__main__":
    main()
