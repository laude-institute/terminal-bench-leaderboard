#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    MOD = 10**9 + 7
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    # Read words: syllable length and rhyme class
    syll_count = [0] * (K + 1)
    words = []  # list of (s, c)
    for _ in range(N):
        s = int(next(it))
        c = int(next(it))
        words.append((s, c))
        if s <= K:
            syll_count[s] += 1
    # DP: number of ways to form i syllables
    dp = [0] * (K + 1)
    dp[0] = 1
    # Precompute available syllable lengths
    lengths = [i for i, cnt in enumerate(syll_count) if cnt > 0]
    for i in range(1, K + 1):
        total = 0
        for t in lengths:
            if t > i:
                break
            total = (total + dp[i - t] * syll_count[t]) % MOD
        dp[i] = total
    # Count ways to end a line with each rhyme class
    rhyme_count = {}
    for s, c in words:
        if s <= K:
            rhyme_count[c] = (rhyme_count.get(c, 0) + dp[K - s]) % MOD
    # Read rhyme scheme letters
    scheme = data[3 + 2*N:]
    # Count occurrences of each letter
    cnt = {}
    for ch in scheme:
        cnt[ch] = cnt.get(ch, 0) + 1
    # For each scheme letter, compute total ways
    result = 1
    for ch, times in cnt.items():
        s = 0
        for rc in rhyme_count.values():
            s = (s + pow(rc, times, MOD)) % MOD
        result = (result * s) % MOD
    # Output result
    print(result)

if __name__ == '__main__':
    main()
