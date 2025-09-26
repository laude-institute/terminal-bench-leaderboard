#!/usr/bin/env python3
"""
Solution for the Mountain Climbing problem (Johnson's rule for two-stage flow shop).
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cows = []
    idx = 1
    # Partition cows into two groups based on U <= D
    group1 = []  # U <= D (schedule early)
    group2 = []  # U > D  (schedule late)
    for _ in range(n):
        u = int(data[idx]); d = int(data[idx+1])
        idx += 2
        if u <= d:
            group1.append((u, d))
        else:
            group2.append((u, d))
    # Sort group1 by ascending U, group2 by descending D
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: -x[1])

    t1 = 0  # time when all ups are done so far
    t2 = 0  # time when all downs are done so far
    # Process in the combined optimal sequence
    for u, d in group1 + group2:
        t1 += u
        # start down only after both t2 and t1
        t2 = max(t2, t1) + d
    # t2 is the makespan
    print(t2)

if __name__ == '__main__':
    main()
