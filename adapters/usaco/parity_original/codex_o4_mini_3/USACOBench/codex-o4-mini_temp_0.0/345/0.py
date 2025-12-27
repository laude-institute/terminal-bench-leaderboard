#!/usr/bin/env python3
"""
Solution to Pogo-Cow problem.
Implements dynamic programming in O(N^2 log N) time.
"""
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    xs = []
    ps = []
    for i in range(N):
        x = int(data[2*i + 1])
        p = int(data[2*i + 2])
        xs.append(x)
        ps.append(p)
    # sort targets by position
    items = sorted(zip(xs, ps))
    xs = [x for x, _ in items]
    ps = [p for _, p in items]
    # dp_dists[j]: sorted list of previous jump distances ending at j
    # dp_maxvals[j]: prefix max of dp values corresponding to dp_dists
    dp_dists = [[0] for _ in range(N)]
    dp_maxvals = [[ps[i]] for i in range(N)]
    ans = max(ps)
    for k in range(N):
        new_entries = []
        # consider jumping from j to k
        for j in range(k):
            d = xs[k] - xs[j]
            # find best dp ending at j with prev jump <= d
            idx = bisect.bisect_right(dp_dists[j], d) - 1
            prev_best = dp_maxvals[j][idx]
            val = prev_best + ps[k]
            new_entries.append((d, val))
            if val > ans:
                ans = val
        # build dp arrays for k
        combined = [(0, ps[k])] + new_entries
        combined.sort(key=lambda x: x[0])
        ds = []
        mv = []
        running = 0
        for d, v in combined:
            ds.append(d)
            running = v if v > running else running
            mv.append(running)
        dp_dists[k] = ds
        dp_maxvals[k] = mv
    print(ans)

if __name__ == '__main__':
    main()
