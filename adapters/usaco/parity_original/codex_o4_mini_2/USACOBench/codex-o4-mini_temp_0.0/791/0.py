#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N, M, K = map(int, data)
    mod = 10**9 + 7
    # Precompute factorials and inverse factorials up to N
    fact = [1] * (N+1)
    for i in range(1, N+1):
        fact[i] = fact[i-1] * i % mod
    invfact = [1] * (N+1)
    invfact[N] = pow(fact[N], mod-2, mod)
    for i in range(N, 0, -1):
        invfact[i-1] = invfact[i] * i % mod
    # Precompute powers of (M-1)
    pow_m1 = [1] * (N+1)
    m1 = (M-1) % mod
    for i in range(1, N+1):
        pow_m1[i] = pow_m1[i-1] * m1 % mod
    # Sum over number of runs R
    # R = 1 case
    ans = M % mod
    # Maximum R for which interior runs can fit
    # For R>=2, S = N-2-(R-2)*K >= 0 => R <= (N-2)//K + 2
    Rmax = (N-2) // K + 2 if N >= 2 else 1
    for R in range(2, Rmax+1):
        S = N - 2 - (R-2) * K
        if S < 0:
            break
        # number of compositions = C(S+R-1, R-1)
        n = S + R - 1
        k = R - 1
        comb = fact[n] * invfact[k] % mod * invfact[n-k] % mod
        ways = M * pow_m1[R-1] % mod * comb % mod
        ans = (ans + ways) % mod
    print(ans)

if __name__ == '__main__':
    main()
