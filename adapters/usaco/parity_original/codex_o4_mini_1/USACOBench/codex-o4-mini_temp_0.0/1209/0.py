#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # Compute allowed gifts for each cow as bitmask
    allowed = [0] * N
    prefs = []
    for i in range(N):
        row = list(map(int, input().split()))
        prefs.append(row)
    for i in range(N):
        # find original gift position
        orig = i+1
        limit = prefs[i].index(orig)
        mask = 0
        for j in range(limit+1):
            mask |= 1 << (prefs[i][j] - 1)
        allowed[i] = mask

    Q = int(input())
    breed_masks = []
    for _ in range(Q):
        s = input().strip()
        mask = 0
        for i,ch in enumerate(s):
            if ch == 'H':
                mask |= 1 << i
        breed_masks.append(mask)

    # Cache for f[mask] = number of perfect matchings for cows/gifts in mask
    f_cache = {}

    def compute_f(mask):
        if mask in f_cache:
            return f_cache[mask]
        # list of cows in mask
        cows = [i for i in range(N) if (mask >> i) & 1]
        k = len(cows)
        # dp over gift subsets for these cows
        dp = [0] * (1 << k)
        dp[0] = 1
        for gm in range(1 << k):
            c = bin(gm).count('1')
            if c >= k:
                continue
            cow = cows[c]
            for j in range(k):
                if not (gm >> j) & 1:
                    gift = cows[j]
                    if (allowed[cow] >> gift) & 1:
                        dp[gm | (1 << j)] += dp[gm]
        res = dp[(1 << k) - 1]
        f_cache[mask] = res
        return res

    full_mask = (1 << N) - 1
    out = []
    for mask in breed_masks:
        other = full_mask ^ mask
        a = compute_f(mask)
        b = compute_f(other)
        out.append(str(a * b))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
