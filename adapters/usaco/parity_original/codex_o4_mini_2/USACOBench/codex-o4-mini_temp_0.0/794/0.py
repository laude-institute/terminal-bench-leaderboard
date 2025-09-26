#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    MOD = 10**9+7
    n = int(next(it))
    R = [0]*n
    for _ in range(n):
        i = int(next(it)); j = int(next(it))
        R[i] = j
    # prefix minima
    P = [0]*n
    P[0] = R[0]
    for x in range(1, n):
        P[x] = P[x-1] if P[x-1] < R[x] else R[x]
    # suffix maxima
    Q = [0]*n
    Q[n-1] = R[n-1]
    for x in range(n-2, -1, -1):
        Q[x] = Q[x+1] if Q[x+1] > R[x] else R[x]
    # prefix sums of P and P^2
    psum = [0]*n
    psum2 = [0]*n
    s = 0; s2 = 0
    for i in range(n):
        s = (s + P[i]) % MOD
        s2 = (s2 + P[i]*P[i]) % MOD
        psum[i] = s
        psum2[i] = s2
    inv2 = (MOD+1)//2
    total = 0
    # binary search helper on P: find first idx where P[idx] <= val
    def find_t(val):
        lo = 0; hi = n-1; ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if P[mid] <= val:
                ans = mid; hi = mid - 1
            else:
                lo = mid + 1
        return ans
    # sum contributions
    for x2 in range(1, n):
        B = Q[x2]
        t = find_t(B-1)
        if t >= x2:
            continue
        k = x2 - t
        # sum P[t..x2-1]
        sumP = psum[x2-1] - (psum[t-1] if t > 0 else 0)
        sumP %= MOD
        sumP2 = psum2[x2-1] - (psum2[t-1] if t > 0 else 0)
        sumP2 %= MOD
        # compute sum_D and sum_D2
        # D_i = B - P[i]
        sum_D = (k * B - sumP) % MOD
        sum_D2 = (k * (B * B % MOD) - 2 * B % MOD * sumP % MOD + sumP2) % MOD
        contrib = (sum_D2 + sum_D) * inv2 % MOD
        total = (total + contrib) % MOD
    # result
    sys.stdout.write(str(total))

if __name__ == '__main__':
    main()
