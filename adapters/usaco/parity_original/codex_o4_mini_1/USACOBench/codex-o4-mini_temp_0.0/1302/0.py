#!/usr/bin/env python3
"""
Solution for the bakery upgrade problem.
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it, 0))
    out = []
    for _ in range(T):
        n = int(next(it))
        tC = int(next(it))
        tM = int(next(it))
        a = []
        b = []
        d = []
        # Precompute di = ci - ai * tC
        for _ in range(n):
            ai = int(next(it)); bi = int(next(it)); ci = int(next(it))
            a.append(ai)
            b.append(bi)
            d.append(ci - ai * tC)
        # Find minimal cookie-upgrades x so that muffin time can stay >=1
        x_low = 0
        for ai, bi, di in zip(a, b, d):
            # Need floor((ai*x + di)/bi) >= 1 => ai*x + di >= bi
            # ai*x >= bi - di => x >= ceil((bi - di)/ai)
            need = bi - di
            if need > 0:
                # ceil division
                Li = (need + ai - 1) // ai
                if Li > x_low:
                    x_low = Li
        # Cannot reduce tC below 1
        if x_low > tC - 1:
            x_low = tC - 1
        # Compute minimal muffin-time multiplier M after x_low upgrades
        M = None
        for ai, bi, di in zip(a, b, d):
            Mi = (ai * x_low + di) // bi
            if M is None or Mi < M:
                M = Mi
        # Muffin time tM' = min(M, tM), but at least 1
        tM_prime = M if M < tM else tM
        # Compute muffin-upgrades y
        y = tM - tM_prime
        # Total cost
        cost = x_low + y
        out.append(str(cost))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
