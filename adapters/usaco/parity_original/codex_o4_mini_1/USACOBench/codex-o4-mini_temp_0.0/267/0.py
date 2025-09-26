#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0].strip()
    t = data[1].strip()
    n = len(s)
    m = len(t)

    # Compute LPS (longest proper prefix which is also suffix)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and t[i] != t[j]:
            j = lps[j-1]
        if t[i] == t[j]:
            j += 1
        lps[i] = j

    # Build automaton next_state[k][c] = next match length
    # states 0..m, but we avoid state m (full match)
    next_state = [ [0]*26 for _ in range(m+1) ]
    for k in range(m+1):
        for ci in range(26):
            c = chr(ord('a') + ci)
            if k < m and c == t[k]:
                next_state[k][ci] = k + 1
            else:
                if k == 0:
                    next_state[k][ci] = 0
                else:
                    next_state[k][ci] = next_state[lps[k-1]][ci]

    # DP: dp[k] = min deletions to reach state k
    INF = n + 1
    dp = [INF] * (m)
    dp[0] = 0
    for ch in s:
        ci = ord(ch) - ord('a')
        new_dp = [INF] * m
        for k in range(m):
            cur = dp[k]
            if cur >= INF:
                continue
            # option 1: delete this char
            if cur + 1 < new_dp[k]:
                new_dp[k] = cur + 1
            # option 2: keep this char
            k2 = next_state[k][ci]
            if k2 < m and cur < new_dp[k2]:
                new_dp[k2] = cur
        dp = new_dp
    # answer is minimal deletions among safe states
    ans = min(dp)
    print(ans)

if __name__ == '__main__':
    main()
