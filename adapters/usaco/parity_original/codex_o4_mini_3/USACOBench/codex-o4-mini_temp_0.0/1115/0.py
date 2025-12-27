#!/usr/bin/env python3
import sys

def count_matches(T, delta):
    # count A in [0, T] such that parity of base-3 digits of A equals that of A+delta
    if T < 0:
        return 0
    # build base-3 digits
    t = []
    x = T
    while x:
        t.append(x % 3)
        x //= 3
    d = []
    y = delta
    while y:
        d.append(y % 3)
        y //= 3
    max_k = max(len(t), len(d)) + 1
    # dp[pos][carry][tight]
    # use two layers
    dp = [[0, 0] for _ in range(2)]
    # carry=0, tight=1
    dp[0][1] = 1
    for pos in range(max_k):
        ndp = [[0, 0] for _ in range(2)]
        tk = t[pos] if pos < len(t) else 0
        dk = d[pos] if pos < len(d) else 0
        for carry in (0, 1):
            for tight in (0, 1):
                cnt = dp[carry][tight]
                if not cnt:
                    continue
                limit = tk if tight else 2
                for ak in range(limit + 1):
                    s = ak + dk + carry
                    out = s % 3
                    c2 = s // 3
                    if (ak & 1) != (out & 1):
                        continue
                    t2 = tight and (ak == tk)
                    ndp[c2][1 if t2 else 0] += cnt
        dp = ndp
    # sum dp with carry=0
    return dp[0][0] + dp[0][1]

def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    out = []
    idx = 1
    for _ in range(q):
        d = int(data[idx]); x = int(data[idx+1]); y = int(data[idx+2])
        idx += 3
        delta = y - x
        # count in [x, x+d]
        res = count_matches(x + d, delta) - count_matches(x - 1, delta)
        out.append(str(res))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
