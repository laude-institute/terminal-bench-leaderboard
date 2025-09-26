#!/usr/bin/env python3
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    N = int(next(it))
    K = int(next(it))
    xs = [0]* (N+1)
    ys = [0]* (N+1)
    for i in range(1, N+1):
        xs[i] = int(next(it))
        ys[i] = int(next(it))
    if T == 2:
        # maximum sum of unmatched weights: weighted independent set
        # compute prev[i]: largest j < i with xs[i] - xs[j] > K
        import bisect
        prev = [0]*(N+1)
        for i in range(1, N+1):
            # find first j where xs[j] >= xs[i] - K + 1
            # so xs[i] - xs[j] > K => xs[j] < xs[i] - K
            lo = bisect.bisect_left(xs, xs[i] - K)
            # xs[lo] >= xs[i]-K, so prev is lo-1
            prev[i] = lo - 1
        dp = [0]*(N+1)
        for i in range(1, N+1):
            # either skip i, or take i
            dp[i] = dp[i-1]
            cand = ys[i] + (dp[prev[i]] if prev[i] >= 0 else 0)
            if cand > dp[i]: dp[i] = cand
        print(dp[N])
    else:
        # T == 1: minimum sum of unmatched weights: greedy sliding window
        import heapq
        matched = [False] * (N+1)
        heap = []  # max-heap by weight
        left = 1
        active_unmatched = 0
        total_unmatched = 0
        for i in range(1, N+1):
            # add cow i
            heapq.heappush(heap, (-ys[i], i))
            active_unmatched += 1
            # expire cows out of window
            while left <= N and xs[i] - xs[left] > K:
                if not matched[left]:
                    # try match left with heaviest neighbor
                    if active_unmatched >= 2:
                        # find heaviest r != left
                        while heap:
                            w, j = heapq.heappop(heap)
                            if not matched[j] and j != left:
                                matched[j] = matched[left] = True
                                active_unmatched -= 2
                                break
                        # clear residual matched entries lazily
                    else:
                        # leave left unmatched
                        total_unmatched += ys[left]
                        active_unmatched -= 1
                # remove left
                left += 1
        # process remaining
        INF = 10**30
        # push sentinel to expire all
        for sentinel in [N+1]:
            # use xs sentinel large
            while left <= N:
                if not matched[left]:
                    if active_unmatched >= 2:
                        while heap:
                            w, j = heapq.heappop(heap)
                            if not matched[j] and j != left:
                                matched[j] = matched[left] = True
                                active_unmatched -= 2
                                break
                    else:
                        total_unmatched += ys[left]
                        active_unmatched -= 1
                left += 1
        print(total_unmatched)


if __name__ == '__main__':
    solve()
