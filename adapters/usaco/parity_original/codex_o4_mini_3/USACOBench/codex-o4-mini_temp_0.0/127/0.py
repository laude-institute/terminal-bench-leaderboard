#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    M, N, L, H, B = map(int, data)
    L2, H2 = L*L, H*H
    mod = B
    res = 0
    # horizontal and vertical segments of length 1
    if L <= 1 <= H:
        if M >= 1:
            res = (res + M * (N+1)) % mod
        if N >= 1:
            res = (res + (M+1) * N) % mod

    # precompute mu and spf up to max_val
    max_val = min(M, H)
    n = max_val
    mu = [1] * (n+1)
    is_prime = [True] * (n+1)
    spf = list(range(n+1))
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i, n+1, i):
                is_prime[j] = False
                mu[j] *= -1
                spf[j] = i if spf[j] == j else spf[j]
            sq = i*i
            for j in range(sq, n+1, sq):
                mu[j] = 0

    # helper to enumerate divisors of x
    def divisors(x):
        # prime factorization
        pf = {}
        while x > 1:
            p = spf[x]
            cnt = 0
            while x % p == 0:
                x //= p
                cnt += 1
            pf[p] = cnt
        # generate
        dvs = [1]
        for p, cnt in pf.items():
            prev = dvs[:]
            mul = 1
            for _ in range(cnt):
                mul *= p
                for d in prev:
                    dvs.append(d * mul)
        return dvs

    # process dx > 0, dy > 0
    for dx in range(1, max_val+1):
        dx2 = dx*dx
        # find dy bounds
        rem_low = L2 - dx2
        a = 0
        if rem_low > 0:
            a = int((rem_low**0.5) // 1)
            if a*a < rem_low:
                a += 1
        a = max(a, 1)
        rem_high = H2 - dx2
        if rem_high < 0:
            continue
        b = int(rem_high**0.5)
        if b > N:
            b = N
        if a > b:
            continue
        # inclusion-exclusion for gcd(dx, dy) == 1
        divs = divisors(dx)
        # count k and sum of dy
        k = 0
        sumdy = 0
        for d in divs:
            mu_d = mu[d]
            if mu_d == 0:
                continue
            lo = (a + d - 1) // d
            hi = b // d
            cnt = hi - lo + 1
            if cnt <= 0:
                continue
            k += mu_d * cnt
            # sum of t from lo to hi
            s = (lo + hi) * cnt // 2
            sumdy += mu_d * d * s
        # placements
        A = M + 1 - dx
        Bn = N + 1
        # weight for dy>0: 2 * A * sum(Bn - dy)
        # sum(Bn - dy) = k*Bn - sumdy
        total = (k * Bn - sumdy) % mod
        res = (res + 2 * A * total) % mod

    print(res)

if __name__ == '__main__':
    main()
