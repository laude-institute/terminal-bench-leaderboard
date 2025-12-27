#!/usr/bin/env python3
import sys
def main():
    import sys, bisect
    MOD = 10**9+7
    data = sys.stdin.read().split()
    N = int(data[0])
    s = list(map(int, data[1:1+N]))
    t = list(map(int, data[1+N:1+2*N]))
    s.sort()
    t.sort()
    # precompute factorials
    fact = [1] * (N+1)
    for i in range(1, N+1): fact[i] = fact[i-1] * i % MOD
    ans = 0
    INF = 10**18
    # iterate k = number of matched cows
    for k in range(0, N+1):
        # threshold for unmatched cows
        th = s[k] if k < N else INF
        # Bk = number of barns with size >= th
        idx = bisect.bisect_left(t, th)
        B = N - idx
        if B > k: continue
        # small barns are t[0:idx]
        Nk = idx
        v = k - B
        # build d_i = number of small barns that can fit cow i
        # cows are s[0:k]
        # prepare list u = t[0:idx]
        u = t[:idx]
        # DP for matching to small barns
        # dp[j] = ways to match j cows among processed
        dp = [0] * (v+1)
        dp[0] = 1
        # process cows in descending order
        for ci in range(k-1, -1, -1):
            si = s[ci]
            # number of small barns >= si
            d = Nk - bisect.bisect_left(u, si)
            # update dp
            # j from min(i+1,v) down to 1
            hi = min(k-ci, v)
            for j in range(hi, 0, -1):
                # choose this cow for small barn
                ways = dp[j-1] * (d - (j-1))
                dp[j] = (dp[j] + ways) % MOD
        # dp[v] is number of ways to match v cows to small barns
        # large barns match the rest B cows, in B! ways
        ways_k = dp[v] * fact[B] % MOD
        ans = (ans + ways_k) % MOD
    print(ans)

if __name__ == '__main__':
    main()
