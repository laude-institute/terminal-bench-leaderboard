#!/usr/bin/env python3
import sys

def main():
    mod = 10**9 + 7
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))

    # Count words by syllable and by rhyme class
    count_by_s = [0] * (K + 1)
    class_syll = {}
    for _ in range(N):
        s = int(next(it))
        c = int(next(it))
        count_by_s[s] += 1
        if c not in class_syll:
            class_syll[c] = {}
        class_syll[c][s] = class_syll[c].get(s, 0) + 1

    # Precompute dp[k]: ways to form k syllables
    dp = [0] * (K + 1)
    dp[0] = 1
    sylls = [s for s in range(1, K+1) if count_by_s[s] > 0]
    for k in range(1, K + 1):
        total = 0
        for s in sylls:
            if s > k:
                break
            total = (total + count_by_s[s] * dp[k - s]) % mod
        dp[k] = total

    # Compute rhyme_count per class: ways to end a line in that class
    rhyme_count = {}
    for c, sdict in class_syll.items():
        rc = 0
        for s, cnt in sdict.items():
            if K - s >= 0:
                rc = (rc + cnt * dp[K - s]) % mod
        rhyme_count[c] = rc

    # Count lines per rhyme scheme letter
    scheme = {}
    for _ in range(M):
        e = next(it)
        scheme[e] = scheme.get(e, 0) + 1

    # Calculate total poems
    result = 1
    for m_i in scheme.values():
        group_sum = 0
        for rc in rhyme_count.values():
            group_sum = (group_sum + pow(rc, m_i, mod)) % mod
        result = result * group_sum % mod

    print(result)


if __name__ == '__main__':
    main()
