#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    MOD = 10**9 + 7

    n = int(input())
    pts = []  # list of (x, y)
    for i in range(n):
        x, y = map(int, input().split())
        pts.append((x, y, i))

    # Prepare containers for sums
    dx = [0] * n
    dy = [0] * n

    # Group by y for horizontal distances
    from collections import defaultdict
    by_y = defaultdict(list)
    for x, y, idx in pts:
        by_y[y].append((x, idx))
    for y, lst in by_y.items():
        lst.sort()
        m = len(lst)
        xs = [x for x, _ in lst]
        idxs = [idx for _, idx in lst]
        # prefix sums of xs
        pre = [0] * m
        pre[0] = xs[0]
        for i in range(1, m):
            pre[i] = pre[i-1] + xs[i]
        total_sum = pre[-1]
        for i in range(m):
            x = xs[i]
            idx = idxs[i]
            # sum of distances to left
            left_count = i
            left_sum = pre[i-1] if i > 0 else 0
            left_dist = x * left_count - left_sum
            # sum of distances to right
            right_count = m - i - 1
            right_sum = total_sum - pre[i]
            right_dist = right_sum - x * right_count
            dx[idx] = (left_dist + right_dist) % MOD

    # Group by x for vertical distances
    by_x = defaultdict(list)
    for x, y, idx in pts:
        by_x[x].append((y, idx))
    for x, lst in by_x.items():
        lst.sort()
        m = len(lst)
        ys = [y for y, _ in lst]
        idxs = [idx for _, idx in lst]
        pre = [0] * m
        pre[0] = ys[0]
        for i in range(1, m):
            pre[i] = pre[i-1] + ys[i]
        total_sum = pre[-1]
        for i in range(m):
            y = ys[i]
            idx = idxs[i]
            left_count = i
            left_sum = pre[i-1] if i > 0 else 0
            left_dist = y * left_count - left_sum
            right_count = m - i - 1
            right_sum = total_sum - pre[i]
            right_dist = right_sum - y * right_count
            dy[idx] = (left_dist + right_dist) % MOD

    # Sum contributions
    ans = 0
    for i in range(n):
        ans = (ans + dx[i] * dy[i]) % MOD
    print(ans)

if __name__ == '__main__':
    main()
