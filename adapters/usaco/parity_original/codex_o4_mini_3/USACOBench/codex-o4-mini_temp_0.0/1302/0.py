#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        N = int(next(it))
        tC = int(next(it)); tM = int(next(it))
        a = []; b = []; c = []
        for i in range(N):
            ai = int(next(it)); bi = int(next(it)); ci = int(next(it))
            a.append(ai); b.append(bi); c.append(ci)
        # compute required upgrades for each friend
        need = []
        for ai, bi, ci in zip(a, b, c):
            req = ai*tC + bi*tM - ci
            if req > 0:
                need.append((ai, bi, req))
        if not need:
            out.append('0'); continue
        best = float('inf')
        # axis intersections
        for ai, bi, req in need:
            # x-axis (y=0)
            x0 = (req + ai - 1) // ai
            if x0 <= tC-1:
                y0 = 0
                # check
                ok = True
                for aj, bj, rj in need:
                    if aj*x0 + bj*y0 < rj:
                        ok = False; break
                if ok:
                    best = min(best, x0 + y0)
            # y-axis (x=0)
            y0 = (req + bi - 1) // bi
            if y0 <= tM-1:
                x0 = 0
                ok = True
                for aj, bj, rj in need:
                    if aj*x0 + bj*y0 < rj:
                        ok = False; break
                if ok:
                    best = min(best, x0 + y0)
        # intersections of pairs
        M = len(need)
        for i in range(M):
            ai, bi, ri = need[i]
            for j in range(i+1, M):
                aj, bj, rj = need[j]
                D = ai * bj - aj * bi
                # ensure positive denominator by ordering
                if D == 0:
                    continue
                if D > 0:
                    a1, b1, r1 = ai, bi, ri
                    a2, b2, r2 = aj, bj, rj
                    D2 = D
                    num_x = r1*b2 - r2*b1
                    num_y = a1*r2 - a2*r1
                else:
                    # swap roles
                    a1, b1, r1 = aj, bj, rj
                    a2, b2, r2 = ai, bi, ri
                    D2 = -D
                    num_x = r1*b2 - r2*b1
                    num_y = a1*r2 - a2*r1
                # require non-negative intersection
                if num_x < 0 or num_y < 0:
                    continue
                # integer ceil
                x0 = (num_x + D2 - 1) // D2
                y0 = (num_y + D2 - 1) // D2
                # bounds
                if x0 > tC-1 or y0 > tM-1:
                    continue
                # check all
                ok = True
                for ak, bk, rk in need:
                    if ak*x0 + bk*y0 < rk:
                        ok = False; break
                if ok:
                    best = min(best, x0 + y0)
        out.append(str(best))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
