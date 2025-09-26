#!/usr/bin/env python3
import sys

def count_upto(N, delta):
    # Count u in [0..N] such that for all base-3 digit positions k,
    # parity(u_k) == parity((u_k + delta_k + carry_in) % 3)
    if N < 0:
        return 0
    # Convert N and delta to base-3 digit lists (MSB first)
    dN = []
    x = N
    while x:
        dN.append(x % 3)
        x //= 3
    if not dN:
        dN = [0]
    L = len(dN)
    dN = dN[::-1]
    dD = []
    x = delta
    for _ in range(L):
        dD.append(x % 3)
        x //= 3
    dD += [0] * (L - len(dD))
    dD = dD[::-1]

    from functools import lru_cache

    @lru_cache(None)
    def dp(pos, carry, tight):
        if pos == L:
            return 1 if carry == 0 else 0
        limit = dN[pos] if tight else 2
        total = 0
        for ud in range(limit + 1):
            s = ud + dD[pos] + carry
            vd = s % 3
            c2 = s // 3
            # parity: digit==1 is odd
            if (ud == 1) != (vd == 1):
                continue
            total += dp(pos + 1, c2, tight and (ud == limit))
        return total

    return dp(0, 0, True)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    Q = int(next(it))
    out = []
    for _ in range(Q):
        d = int(next(it))
        x = int(next(it))
        y = int(next(it))
        if y >= x:
            delta = y - x
            A = x
        else:
            delta = x - y
            A = y
        B = A + d
        # count u in [A..B]
        ans = count_upto(B, delta) - count_upto(A-1, delta)
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
