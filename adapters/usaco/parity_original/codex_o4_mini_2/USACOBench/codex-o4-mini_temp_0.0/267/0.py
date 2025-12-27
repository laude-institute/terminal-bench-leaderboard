"""
Solution to Problem 3: Necklace

We use dynamic programming with KMP automaton to avoid substring matches.
DP[i][j]: min deletions after i chars, in prefix match state j.
Roll arrays to O(M) space.
"""
import sys

def build_kmp(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j-1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    # build transition table
    go = [ [0] * 26 for _ in range(m+1) ]
    for state in range(m+1):
        for c in range(26):
            if state < m and ord(pattern[state]) - ord('a') == c:
                go[state][c] = state + 1
            else:
                if state == 0:
                    go[state][c] = 0
                else:
                    go[state][c] = go[pi[state-1]][c]
    return pi, go

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    n, m = len(s), len(t)
    pi, go = build_kmp(t)
    INF = n + 5
    # dp[j]: min deletions at current pos, matching length j
    dp = [INF] * m
    dp[0] = 0
    for ch in s:
        c = ord(ch) - ord('a')
        ndp = [INF] * m
        for j in range(m):
            if dp[j] >= INF:
                continue
            # delete ch
            if dp[j] + 1 < ndp[j]:
                ndp[j] = dp[j] + 1
            # keep ch
            nj = go[j][c]
            if nj < m and dp[j] < ndp[nj]:
                ndp[nj] = dp[j]
        dp = ndp
    # answer is min over j
    print(min(dp))

if __name__ == '__main__':
    main()
