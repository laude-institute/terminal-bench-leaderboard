#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    flavors = [0] * N
    spiciness = [0] * N
    for i in range(N):
        f, s = map(int, input().split())
        flavors[i] = f
        spiciness[i] = s

    dq = deque()  # will store indices with decreasing spiciness
    ans = float('inf')
    sum_f = 0
    left = 0

    for right in range(N):
        sum_f += flavors[right]
        # maintain deque for max spiciness
        while dq and spiciness[dq[-1]] <= spiciness[right]:
            dq.pop()
        dq.append(right)

        # shrink window while flavor sum meets requirement
        while sum_f >= M:
            ans = min(ans, spiciness[dq[0]])
            if dq[0] == left:
                dq.popleft()
            sum_f -= flavors[left]
            left += 1

    print(ans)

if __name__ == '__main__':
    main()
