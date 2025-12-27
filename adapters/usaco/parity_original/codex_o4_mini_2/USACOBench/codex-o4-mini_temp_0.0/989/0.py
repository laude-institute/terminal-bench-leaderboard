#!/usr/bin/env python3
import sys
import math

def max_dist(T, X):
    P = (T + X) // 2
    if P > T:
        P = T
    # sum of speeds up to P (increasing phase)
    S1 = P * (P + 1) // 2
    # remaining time after P (steady/decreasing phase)
    rem = T - P
    # sum of time indices from P+1 to T
    sum_t = (P + 1 + T) * rem // 2
    # sum of speeds in remaining phase
    S2 = rem * (X + T) - sum_t
    return S1 + S2

def main():
    data = sys.stdin.read().split()
    K = int(data[0])
    N = int(data[1])
    Xs = list(map(int, data[2:]))
    # precompute upper bound for binary search
    sqrtK = int(math.sqrt(K))
    maxX = max(Xs) if Xs else 0
    high = 2 * sqrtK + 2 * maxX + 10
    out = []
    for X in Xs:
        lo, hi = 0, high
        while lo < hi:
            mid = (lo + hi) // 2
            if max_dist(mid, X) >= K:
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
