#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin
    n, m = map(int, data.readline().split())
    F = [0] * n
    S = [0] * n
    for i in range(n):
        f, s = map(int, data.readline().split())
        F[i] = f
        S[i] = s

    left = 0
    total_flavor = 0
    answer = 10**18
    dq = deque()  # stores pairs (spiciness, index), monotonic decreasing

    for right in range(n):
        total_flavor += F[right]
        # maintain deque for max spiciness
        while dq and dq[-1][0] < S[right]:
            dq.pop()
        dq.append((S[right], right))

        # shrink window while flavor requirement met
        while total_flavor >= m:
            # current window spiciness is dq[0][0]
            answer = min(answer, dq[0][0])
            # remove left element
            if dq and dq[0][1] == left:
                dq.popleft()
            total_flavor -= F[left]
            left += 1

    print(answer)

if __name__ == '__main__':
    main()
