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
    c = list(map(int, it))
    c.sort()
    # prefix sums of citations
    P = [0] * (N + 1)
    for i in range(N):
        P[i+1] = P[i] + c[i]

    max_citations = K * L

    def can(h):
        # check if h-index h is achievable
        if h == 0:
            return True
        # count papers with citations >= h
        pos = bisect.bisect_left(c, h)
        big = N - pos
        # count papers that can be raised to h (with at most K citations)
        # those with c[i] >= h-K
        threshold = h - K
        if threshold <= 0:
            idx_l = 0
        else:
            idx_l = bisect.bisect_left(c, threshold)
        small = pos - idx_l
        # need total papers >= h
        if big + small < h:
            return False
        # need to raise k papers
        k = h - big
        if k <= 0:
            return True
        # choose k papers with largest c[i] among candidates
        # these are the last k in c[idx_l:pos]
        # sum of their citations:
        sum_c = P[pos] - P[pos-k]
        # total citations needed
        needed = k * h - sum_c
        return needed <= max_citations

    # binary search for maximum h
    lo, hi = 0, N + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            lo = mid + 1
        else:
            hi = mid
    # lo is first failing, so answer is lo-1
    print(lo - 1)

if __name__ == '__main__':
    main()
