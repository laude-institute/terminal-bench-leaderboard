#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, K, L = map(int, data[:3])
    c = list(map(int, data[3:3+N]))
    c.sort()
    # prefix sums for sorted citations
    S = [0] * (N + 1)
    for i in range(N):
        S[i+1] = S[i] + c[i]

    import bisect
    # check if an h-index of h is achievable
    def feasible(h):
        # count of papers already with >= h citations
        idx_high = bisect.bisect_left(c, h)
        have = N - idx_high
        if have >= h:
            return True
        # need more papers: R = h - have
        # eligible papers have c_i >= h-K
        idx_low = bisect.bisect_left(c, h - K)
        R = h - have
        # number of eligible papers
        E = idx_high - idx_low
        if R > E:
            return False
        # choose R with largest citations to minimize added citations
        # sum of chosen citations
        sum_c = S[idx_high] - S[idx_high - R]
        # total added citations needed
        needed = R * h - sum_c
        return needed <= K * L

    # binary search max h
    lo, hi = 0, N + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    print(lo)

if __name__ == '__main__':
    main()
