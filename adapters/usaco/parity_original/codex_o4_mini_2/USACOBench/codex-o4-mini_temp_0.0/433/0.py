#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []
    for _ in range(N):
        x, t = input().split()
        x = int(x)
        # white = +1, spotted = -1
        a = 1 if t == 'W' else -1
        cows.append((x, a))
    # sort by position
    cows.sort()
    xs = [0] * (N + 1)
    a = [0] * (N + 1)
    for i, (x, ai) in enumerate(cows, start=1):
        xs[i] = x
        a[i] = ai
    # prefix sums
    pref = [0] * (N + 1)
    for i in range(1, N + 1):
        pref[i] = pref[i - 1] + a[i]
    best = 0
    # process each parity separately
    for parity in (0, 1):
        stack = []  # candidate start indices
        # build decreasing stack of prefix values
        for i in range(N):  # i = 0..N-1
            if (pref[i] & 1) == parity:
                if not stack or pref[i] < pref[stack[-1]]:
                    stack.append(i)
        # scan from end to start
        for j in range(N, 0, -1):
            if (pref[j] & 1) == parity:
                while stack and pref[j] >= pref[stack[-1]]:
                    i = stack.pop()
                    # interval from i+1 to j
                    start_pos = xs[i + 1]
                    best = max(best, xs[j] - start_pos)
    print(best)

if __name__ == '__main__':
    main()
