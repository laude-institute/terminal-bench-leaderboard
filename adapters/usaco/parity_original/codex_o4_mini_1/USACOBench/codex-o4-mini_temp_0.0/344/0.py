#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    N, D = map(int, data[:2])
    cows = []
    idx = 2
    for _ in range(N):
        x = int(data[idx]); h = int(data[idx+1])
        cows.append((x, h))
        idx += 2
    # Sort cows by position
    cows.sort(key=lambda ch: ch[0])
    xs = [cows[i][0] for i in range(N)]
    hs = [cows[i][1] for i in range(N)]
    # Compute max height within D to the left of each cow
    left_max = [0] * N
    dq = deque()  # stores indices in decreasing height
    j = 0
    for i in range(N):
        # shrink window
        while j < i and xs[i] - xs[j] > D:
            if dq and dq[0] == j:
                dq.popleft()
            j += 1
        # record max height in window
        left_max[i] = hs[dq[0]] if dq else 0
        # add current cow
        while dq and hs[dq[-1]] <= hs[i]:
            dq.pop()
        dq.append(i)
    # Compute max height within D to the right of each cow
    right_max = [0] * N
    dq = deque()
    k = N - 1
    for i in range(N-1, -1, -1):
        # shrink window
        while k > i and xs[k] - xs[i] > D:
            if dq and dq[0] == k:
                dq.popleft()
            k -= 1
        # record max height in window
        right_max[i] = hs[dq[0]] if dq else 0
        # add current cow
        while dq and hs[dq[-1]] <= hs[i]:
            dq.pop()
        dq.append(i)
    # Count crowded cows
    count = 0
    for i in range(N):
        if left_max[i] >= 2 * hs[i] and right_max[i] >= 2 * hs[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
