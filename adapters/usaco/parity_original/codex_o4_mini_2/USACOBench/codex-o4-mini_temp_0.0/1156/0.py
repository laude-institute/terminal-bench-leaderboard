#!/usr/bin/env python3
"""
Compute minimum number of range increment/decrement operations
to transform initial temperatures to preferred temperatures.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read preferred and initial temperatures
    p = [int(next(it)) for _ in range(n)]
    t = [int(next(it)) for _ in range(n)]

    inc_ops = 0  # operations to increase segments
    dec_ops = 0  # operations to decrease segments
    prev_pos = 0
    prev_neg = 0
    for i in range(n):
        diff = p[i] - t[i]
        # positive and negative parts of diff
        cur_pos = diff if diff > 0 else 0
        cur_neg = -diff if diff < 0 else 0
        # count extra increase operations needed
        if cur_pos > prev_pos:
            inc_ops += cur_pos - prev_pos
        # count extra decrease operations needed
        if cur_neg > prev_neg:
            dec_ops += cur_neg - prev_neg
        prev_pos = cur_pos
        prev_neg = cur_neg

    # total operations is sum of inc and dec
    print(inc_ops + dec_ops)

if __name__ == '__main__':
    main()
