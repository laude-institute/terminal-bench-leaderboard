#!/usr/bin/env python3
import sys

def possible(positions, B, N, K, L):
    # Build queries for all breeds with freq >= L
    queries = [[] for _ in range(N+1)]  # queries[r] = list of l's
    any_q = False
    for pos_list in positions.values():
        m = len(pos_list)
        if m < L:
            continue
        any_q = True
        for i in range(m - L + 1):
            l = pos_list[i]
            r = pos_list[i+L-1]
            queries[r].append(l)
    if not any_q:
        return False
    # Fenwick tree for distinct count
    BIT = [0] * (N+2)
    def bit_add(i, v):
        while i <= N:
            BIT[i] += v
            i += i & -i
    def bit_sum(i):
        s = 0
        while i > 0:
            s += BIT[i]
            i -= i & -i
        return s

    last = {}
    # Sweep through array
    for i in range(1, N+1):
        x = B[i]
        if x in last:
            bit_add(last[x], -1)
        bit_add(i, 1)
        last[x] = i
        # Process queries ending at i
        for l in queries[i]:
            # total distinct in [l..i]
            tot = bit_sum(i) - bit_sum(l-1)
            # exclude target breed itself: tot includes the breed at endpoints
            # we want tot <= K+1
            if tot <= K+1:
                return True
    return False

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    B = [0] * (N+1)
    positions = {}
    for i in range(1, N+1):
        b = int(data[2 + i - 1])
        B[i] = b
        positions.setdefault(b, []).append(i)
    # binary search on answer L
    lo, hi = 1, max(len(v) for v in positions.values())
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(positions, B, N, K, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)

if __name__ == '__main__':
    main()
