#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    spotty = [input().strip() for _ in range(N)]
    plain = [input().strip() for _ in range(N)]

    # Map characters to integers
    code = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    base = 127
    mod1 = 10**9 + 7
    mod2 = 10**9 + 9

    # Precompute powers
    pow1 = [1] * (M + 1)
    pow2 = [1] * (M + 1)
    for i in range(1, M + 1):
        pow1[i] = (pow1[i-1] * base) % mod1
        pow2[i] = (pow2[i-1] * base) % mod2

    # Compute prefix hashes
    def build_hashes(arr):
        ph = []
        for s in arr:
            h1 = [0] * (M + 1)
            h2 = [0] * (M + 1)
            for i, ch in enumerate(s, 1):
                v = code[ch]
                h1[i] = (h1[i-1] * base + v) % mod1
                h2[i] = (h2[i-1] * base + v) % mod2
            ph.append((h1, h2))
        return ph

    spot_hash = build_hashes(spotty)
    plain_hash = build_hashes(plain)

    # Get hash of substring [l, r) for prefix arrays h1, h2
    def get_hash(h1, h2, l, r):
        x1 = (h1[r] - h1[l] * pow1[r-l]) % mod1
        x2 = (h2[r] - h2[l] * pow2[r-l]) % mod2
        return (x1, x2)

    # Check if any window of length L distinguishes
    def check(L):
        for i in range(M - L + 1):
            seen = set()
            # spotty hashes
            for h1, h2 in spot_hash:
                seen.add(get_hash(h1, h2, i, i+L))
            # plain hashes
            valid = True
            for h1, h2 in plain_hash:
                if get_hash(h1, h2, i, i+L) in seen:
                    valid = False
                    break
            if valid:
                return True
        return False

    # Binary search minimal length
    lo, hi = 1, M
    ans = M
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)

if __name__ == '__main__':
    main()
