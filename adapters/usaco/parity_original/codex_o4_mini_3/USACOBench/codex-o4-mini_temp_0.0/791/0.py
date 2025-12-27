#!/usr/bin/env python3
import sys

def main():
    mod = 10**9+7
    data = sys.stdin.read().strip().split()
    N, M, K = map(int, data)
    # dp_len[l] = number of ways ending with a run of length l (1 <= l < K)
    # dp_L = number of ways ending with a run of length >= K
    from collections import deque
    dp_len = deque([0] * (K-1))  # index 0 for run length 1
    dp_L = 0
    # Initialize for length = 1
    if N >= 1:
        dp_len[0] = M % mod
    # iterate through positions 2..N
    for _ in range(2, N+1):
        # extract count for run length K-1
        p = dp_len[-1] if K > 1 else 0
        # compute new dp_L: extend previous long runs and those reaching length K
        new_dp_L = (dp_L + p) % mod
        # compute new run length 1 from color changes allowed when prev run len >=K or ==K-1
        change_sources = (dp_L + p) % mod
        new_dp_len1 = change_sources * (M-1) % mod
        # shift dp_len right to represent increasing run lengths
        if K > 1:
            dp_len.rotate(1)
            dp_len[0] = new_dp_len1
        dp_L = new_dp_L
    # total ways = sum of dp_len runs and dp_L
    total = dp_L
    total = (total + sum(dp_len)) % mod if K > 1 else total
    print(total)

if __name__ == '__main__':
    main()
