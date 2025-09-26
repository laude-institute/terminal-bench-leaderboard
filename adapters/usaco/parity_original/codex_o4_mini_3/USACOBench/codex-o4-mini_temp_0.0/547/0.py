#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    bales = []
    idx = 1
    for _ in range(n):
        size = int(data[idx]); pos = int(data[idx+1])
        idx += 2
        bales.append((pos, size))
    # Sort bales by position
    bales.sort()
    intervals = []
    # Find all trapped intervals where width <= both bale sizes
    for i in range(n - 1):
        pi, si = bales[i]
        for j in range(i + 1, n):
            pj, sj = bales[j]
            width = pj - pi
            # If width exceeds left bale size, no further j will work
            if width > si:
                break
            # Check right bale size
            if width <= sj:
                intervals.append((pi, pj))
    # Merge intervals and compute total trapped length
    if not intervals:
        print(0)
        return
    intervals.sort()
    total = 0
    cur_l, cur_r = intervals[0]
    for l, r in intervals[1:]:
        if l > cur_r:
            total += cur_r - cur_l
            cur_l, cur_r = l, r
        else:
            cur_r = max(cur_r, r)
    total += cur_r - cur_l
    print(total)

if __name__ == "__main__":
    main()
