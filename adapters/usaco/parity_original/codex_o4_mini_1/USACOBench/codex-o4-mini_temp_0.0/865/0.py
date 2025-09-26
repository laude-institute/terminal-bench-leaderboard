#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    # Build position by ID (1..N)
    P = [0] * N
    for idx, cow in enumerate(A):
        P[cow-1] = idx
    # lis_start: length of LIS ending at each ID index
    from bisect import bisect_left
    lis_start = [0] * N
    tail = []  # will store increasing positions
    for i in range(N):
        x = P[i]
        pos = bisect_left(tail, x)
        if pos == len(tail):
            tail.append(x)
        else:
            tail[pos] = x
        lis_start[i] = pos + 1
    L = len(tail)
    # lis_end: length of LIS starting at each ID index
    # compute on reversed with negation to capture suffix LIS
    B = [-x for x in reversed(P)]
    lis_B = [0] * N
    tail = []
    for j in range(N):
        x = B[j]
        pos = bisect_left(tail, x)
        if pos == len(tail):
            tail.append(x)
        else:
            tail[pos] = x
        lis_B[j] = pos + 1
    lis_end = [0] * N
    for i in range(N):
        lis_end[i] = lis_B[N-1-i]
    # Identify candidate and mandatory deletions
    candidates = []  # IDs (1-based)
    mandatory = []
    for i in range(N):
        if lis_start[i] + lis_end[i] - 1 == L:
            candidates.append(i+1)
        else:
            mandatory.append(i+1)
    D = N - L
    m = len(mandatory)
    R = D - m
    # Prepare result deletions: include all mandatory, plus R from candidates
    res = []
    INF = 10**18
    # combinatorial function with cap
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        k = min(k, n-k)
        res = 1
        # compute multiplicatively, cap at INF
        for i in range(1, k+1):
            res = res * (n - k + i) // i
            if res > INF:
                return INF
        return res
    # Select R elements from candidates by lex
    k = K
    if R < 0:
        R = 0
    chosen = []
    c = len(candidates)
    for idx, cid in enumerate(candidates):
        if R == 0:
            break
        rem = c - idx
        # count if pick this one
        cnt = comb(rem-1, R-1)
        if k <= cnt:
            chosen.append(cid)
            R -= 1
        else:
            k -= cnt
            # skip
    # merge mandatory and chosen
    S = sorted(mandatory + chosen)
    # output
    out = [str(len(S))]
    out += [str(x) for x in S]
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
