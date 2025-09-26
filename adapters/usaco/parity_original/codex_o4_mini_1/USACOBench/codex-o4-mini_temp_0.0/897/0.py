#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it)); K = int(next(it))
    # Read words and count syllable frequencies
    words = []
    count_s = [0] * (K + 1)
    for _ in range(N):
        s = int(next(it)); c = int(next(it))
        words.append((s, c))
        if s <= K:
            count_s[s] += 1

    MOD = 1000000007
    # DP: number of ways to build lines of i syllables
    dp = [0] * (K + 1)
    dp[0] = 1
    for s in range(1, K + 1):
        cs = count_s[s]
        if cs:
            for i in range(s, K + 1):
                dp[i] = (dp[i] + dp[i - s] * cs) % MOD

    # Count ways to end a line with rhyme class c
    rhyme_count = {}
    for s, c in words:
        if s <= K:
            ways = dp[K - s]
            rhyme_count[c] = (rhyme_count.get(c, 0) + ways) % MOD

    # Read rhyme scheme and count frequencies
    freq = {}
    for _ in range(M):
        e = next(it)
        freq[e] = freq.get(e, 0) + 1

    # Compute total poems
    ans = 1
    for f in freq.values():
        total = 0
        for rc in rhyme_count.values():
            total = (total + pow(rc, f, MOD)) % MOD
        ans = ans * total % MOD

    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
