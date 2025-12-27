#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    intervals = []
    for _ in range(n):
        a = int(next(it)); b = int(next(it))
        intervals.append((a, b))
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    # 1-based arrays, add dummy at index 0
    start = [0] * (n+1)
    end = [0] * (n+1)
    for i, (a, b) in enumerate(intervals, start=1):
        start[i] = a
        end[i] = b
    # DP arrays: dp_current[i][j] = max programs using first p-1 intervals,
    # last on tuner1 is i, tuner2 is j
    dp_current = [[-1] * (n+1) for _ in range(n+1)]
    dp_current[0][0] = 0
    for p in range(1, n+1):
        dp_next = [[-1] * (n+1) for _ in range(n+1)]
        sp, ep = start[p], end[p]
        for i in range(0, n+1):
            ei = end[i] if i > 0 else 0
            for j in range(0, n+1):
                cur = dp_current[i][j]
                if cur < 0:
                    continue
                # skip interval p
                if dp_next[i][j] < cur:
                    dp_next[i][j] = cur
                # assign to tuner1
                if sp >= ei:
                    if dp_next[p][j] < cur + 1:
                        dp_next[p][j] = cur + 1
                # assign to tuner2
                ej = end[j] if j > 0 else 0
                if sp >= ej:
                    if dp_next[i][p] < cur + 1:
                        dp_next[i][p] = cur + 1
        dp_current = dp_next
    # result is max over dp_current
    result = 0
    for row in dp_current:
        m = max(row)
        if m > result:
            result = m
    print(result)

if __name__ == '__main__':
    main()
