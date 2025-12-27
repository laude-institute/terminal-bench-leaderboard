#!/usr/bin/env python3
import sys

def count_cows_on_diagonal(x, y, d):
    # Ensure c >= 0 by swapping if needed
    if y < x:
        x, y = y, x
    c = y - x
    # Convert to base-3 digits (MSB first)
    def to_base3(n):
        if n == 0:
            return [0]
        digs = []
        while n:
            digs.append(n % 3)
            n //= 3
        return digs[::-1]

    dx = to_base3(x)
    dc = to_base3(c)
    dd = to_base3(d)
    L = max(len(dx), len(dc), len(dd))
    # Pad with leading zeros
    dx = [0] * (L - len(dx)) + dx
    dc = [0] * (L - len(dc)) + dc
    dd = [0] * (L - len(dd)) + dd

    from functools import lru_cache

    @lru_cache(None)
    def dp(pos, tight, carry1, carry2):
        if pos == L:
            return 1
        total = 0
        max_i = dd[pos] if tight else 2
        for ik in range(max_i + 1):
            ntight = tight and (ik == max_i)
            # add x + i
            s1 = dx[pos] + ik + carry1
            ak = s1 % 3
            nc1 = s1 // 3
            # add c to (x+i)
            s2 = ak + dc[pos] + carry2
            bk = s2 % 3
            nc2 = s2 // 3
            # parity check
            if (ak & 1) != (bk & 1):
                continue
            total += dp(pos + 1, ntight, nc1, nc2)
        return total

    return dp(0, True, 0, 0)

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    Q = int(next(it))
    out = []
    for _ in range(Q):
        d = int(next(it))
        x = int(next(it))
        y = int(next(it))
        out.append(str(count_cows_on_diagonal(x, y, d)))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
