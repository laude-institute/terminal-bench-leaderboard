#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    # read grid and build cow presence matrix
    cows = []
    for _ in range(N):
        row = list(next(it))
        cows.append([1 if c == '*' else 0 for c in row])

    count = 0
    # iterate over possible base endpoints
    for i in range(N):
        for j in range(N):
            if cows[i][j] == 0:
                continue
            # horizontal base
            t_max_h = (N - 1 - j) // 2
            for t in range(1, t_max_h + 1):
                if cows[i][j + 2*t] == 1:
                    mid_j = j + t
                    # apex above
                    up_i = i - t
                    if up_i >= 0 and cows[up_i][mid_j]:
                        count += 1
                    # apex below
                    down_i = i + t
                    if down_i < N and cows[down_i][mid_j]:
                        count += 1
            # vertical base
            t_max_v = (N - 1 - i) // 2
            for t in range(1, t_max_v + 1):
                if cows[i + 2*t][j] == 1:
                    mid_i = i + t
                    # apex left
                    left_j = j - t
                    if left_j >= 0 and cows[mid_i][left_j]:
                        count += 1
                    # apex right
                    right_j = j + t
                    if right_j < N and cows[mid_i][right_j]:
                        count += 1

    print(count)

if __name__ == '__main__':
    main()
