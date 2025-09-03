#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        # read N, t_C, t_M, skipping blank lines
        parts = input().split()
        while not parts:
            parts = input().split()
        N, tC, tM = map(int, parts)
        # compute required reductions for each friend
        req = []  # list of (a, b, r)
        for _ in range(N):
            a, b, c = map(int, input().split())
            r = a * tC + b * tM - c
            if r > 0:
                req.append((a, b, r))
        # if no reductions needed
        if not req:
            print(0)
            continue

        # check feasibility for a given total cost K
        def feasible(K):
            # x <= tC-1, y <= tM-1, x+y <= K => x in [max(0, K-(tM-1)), min(tC-1, K)]
            x_low = max(0, K - (tM - 1))
            x_high = min(tC - 1, K)
            if x_low > x_high:
                return False
            for a, b, r in req:
                # require a*x + b*y >= r and y = K-x
                # => x*(a-b) + b*K >= r
                d = a - b
                if d == 0:
                    if b * K < r:
                        return False
                elif d > 0:
                    # x >= ceil((r - b*K) / d)
                    num = r - b * K
                    # ceil division works for negative and positive
                    tmp = (num + d - 1) // d
                    if tmp > x_low:
                        x_low = tmp
                else:
                    # d < 0: x <= floor((r - b*K) / d)
                    num = r - b * K
                    tmp = num // d
                    if tmp < x_high:
                        x_high = tmp
                if x_low > x_high:
                    return False
            return True

        # binary search minimum K
        lo, hi = 0, (tC - 1) + (tM - 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        print(lo)

if __name__ == '__main__':
    main()
