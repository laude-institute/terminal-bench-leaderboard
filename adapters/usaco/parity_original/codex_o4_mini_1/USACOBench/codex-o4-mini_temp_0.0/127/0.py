#!/usr/bin/env python3
import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    M, N, L, H, B = map(int, data)
    # Precompute Möbius function and divisors up to max(M,N)
    limit = max(M, N)
    mu = [1] * (limit+1)
    is_prime = [True] * (limit+1)
    primes = []
    for i in range(2, limit+1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > limit:
                break
            is_prime[i*p] = False
            if i % p == 0:
                mu[i*p] = 0
                break
            else:
                mu[i*p] = -mu[i]
    # build divisors list
    divisors = [[] for _ in range(limit+1)]
    for d in range(1, limit+1):
        for multiple in range(d, limit+1, d):
            divisors[multiple].append(d)

    total = 0
    L2 = L*L
    H2 = H*H
    # handle dx>=1, dy>=1
    for dx in range(1, min(M, H) + 1):
        dx2 = dx*dx
        lowy2 = max(1, L2 - dx2)
        highy2 = H2 - dx2
        if highy2 < 1:
            continue
        # compute dy bounds
        a = math.isqrt(lowy2)
        if a*a < lowy2:
            a += 1
        b = math.isqrt(highy2)
        if a > b:
            continue
        if a > N:
            continue
        b = min(b, N)
        # count and sum dy with gcd(dx,dy)=1
        cnt = 0
        sum_dy = 0
        for d in divisors[dx]:
            mu_d = mu[d]
            if mu_d == 0:
                continue
            lo = (a + d - 1) // d
            hi = b // d
            if lo > hi:
                continue
            c = hi - lo + 1
            cnt += mu_d * c
            # sum k from lo to hi: (lo+hi)*c//2
            s_k = (lo + hi) * c // 2
            sum_dy += mu_d * d * s_k
        # S(dx) = sum (N+1-dy) = (N+1)*cnt - sum_dy
        S = ( (N+1) * cnt - sum_dy )
        # placements: (M+1-dx)
        placements = (M+1 - dx)
        total = (total + placements * S) % B
    # vertical segments dx=0, dy=1
    if 1 <= N and L <= 1 <= H:
        total = (total + (M+1) * N) % B
    # horizontal segments dy=0, dx=1
    if 1 <= M and L <= 1 <= H:
        total = (total + M * (N+1)) % B
    print(total)

if __name__ == '__main__':
    main()
