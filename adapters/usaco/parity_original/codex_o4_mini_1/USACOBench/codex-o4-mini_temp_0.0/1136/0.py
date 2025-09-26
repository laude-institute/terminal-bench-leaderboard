#!/usr/bin/env python3
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    L = int(next(it))
    c = [int(next(it)) for _ in range(N)]
    c.sort()
    # Prefix sums for c
    ps = [0] * (N + 1)
    for i in range(N):
        ps[i+1] = ps[i] + c[i]
    total_extra = K * L

    def can(h):
        # Number of papers already >= h
        r = bisect.bisect_left(c, h)
        cnt_high = N - r
        if cnt_high >= h:
            return True
        # Need to boost 'need' papers
        need = h - cnt_high
        # Papers with citations >= h-K can be boosted within K
        low_val = h - K
        if low_val <= 0:
            l = 0
        else:
            l = bisect.bisect_left(c, low_val)
        # Check sufficient candidates
        if r - l < need:
            return False
        # Sum of citations of the 'need' largest candidates in [l, r)
        sum_c = ps[r] - ps[r-need]
        # Total extra citations needed
        cost = need * h - sum_c
        return cost <= total_extra

    # Binary search for maximum h
    lo, hi = 0, N + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid
    # Output result
    print(lo)

if __name__ == '__main__':
    main()
