#!/usr/bin/env python3
import sys
def main():
    import sys
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    # Prepare arrays for sum of vertical and horizontal distances
    A = [0] * N  # sum of vertical distances for each point
    B = [0] * N  # sum of horizontal distances for each point
    from collections import defaultdict
    map_x = defaultdict(list)
    map_y = defaultdict(list)
    for i, (x, y) in enumerate(points):
        map_x[x].append((y, i))
        map_y[y].append((x, i))
    # Compute vertical sums A
    for x, lst in map_x.items():
        lst.sort()
        ys = [y for y, _ in lst]
        prefix = [0]
        for y in ys:
            prefix.append(prefix[-1] + y)
        total = prefix[-1]
        cnt = len(ys)
        for idx, (y, i) in enumerate(lst):
            lower = y * idx - prefix[idx]
            upper = (total - prefix[idx+1]) - y * (cnt - idx - 1)
            A[i] = (lower + upper) % MOD
    # Compute horizontal sums B
    for y, lst in map_y.items():
        lst.sort()
        xs = [x for x, _ in lst]
        prefix = [0]
        for x in xs:
            prefix.append(prefix[-1] + x)
        total = prefix[-1]
        cnt = len(xs)
        for idx, (x, i) in enumerate(lst):
            lower = x * idx - prefix[idx]
            upper = (total - prefix[idx+1]) - x * (cnt - idx - 1)
            B[i] = (lower + upper) % MOD
    # Sum contributions
    res = 0
    for i in range(N):
        res = (res + A[i] * B[i]) % MOD
    print(res)

if __name__ == "__main__":
    main()
