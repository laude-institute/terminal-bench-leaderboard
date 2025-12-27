#!/usr/bin/env python3
import sys

def main():
    mod = 10**9 + 7
    data = sys.stdin.read().split()
    n = int(data[0])
    xs = [0] * n
    ys = [0] * n
    idx = 1
    for i in range(n):
        xs[i] = int(data[idx]); ys[i] = int(data[idx+1])
        idx += 2
    from collections import defaultdict
    x_groups = defaultdict(list)
    y_groups = defaultdict(list)
    for i, (x, y) in enumerate(zip(xs, ys)):
        x_groups[x].append((y, i))
        y_groups[y].append((x, i))

    sum_abs_y = [0] * n
    # Compute sum of |y_j - y_i| for same x
    for arr in x_groups.values():
        arr.sort()
        k = len(arr)
        total = sum(y for y, _ in arr)
        prefix = 0
        for j, (y, i) in enumerate(arr):
            prefix_before = prefix
            prefix += y
            lower = y * j - prefix_before
            higher = (total - prefix) - y * (k - j - 1)
            sum_abs_y[i] = (lower + higher) % mod

    sum_abs_x = [0] * n
    # Compute sum of |x_j - x_i| for same y
    for arr in y_groups.values():
        arr.sort()
        k = len(arr)
        total = sum(x for x, _ in arr)
        prefix = 0
        for j, (x, i) in enumerate(arr):
            prefix_before = prefix
            prefix += x
            lower = x * j - prefix_before
            higher = (total - prefix) - x * (k - j - 1)
            sum_abs_x[i] = (lower + higher) % mod

    result = 0
    for i in range(n):
        result = (result + sum_abs_x[i] * sum_abs_y[i]) % mod
    print(result)


if __name__ == '__main__':
    main()
