#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0]); K = int(data[1])
    sizes = list(map(int, data[2:]))
    sizes.sort()
    N = len(sizes)
    win_size = [0] * N
    R = [0] * N
    j = 0
    for i in range(N):
        while j < N and sizes[j] - sizes[i] <= K:
            j += 1
        R[i] = j - 1
        win_size[i] = j - i
    # compute suffix maximums
    suffix = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        suffix[i] = max(win_size[i], suffix[i + 1])
    ans = 0
    for i in range(N):
        total = win_size[i]
        nxt = R[i] + 1
        if nxt < N:
            total += suffix[nxt]
        ans = max(ans, total)
    print(ans)

if __name__ == "__main__":
    main()
