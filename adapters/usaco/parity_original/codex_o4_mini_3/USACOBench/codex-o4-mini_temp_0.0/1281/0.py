#!/usr/bin/env python3
import sys
import threading

def main():
    data = sys.stdin
    l, r, n = map(int, data.readline().split())
    ops_c = [0] * (n + 1)
    ops_s = [''] * (n + 1)
    for i in range(1, n + 1):
        line = data.readline().split()
        ops_c[i] = ord(line[0]) - 97
        ops_s[i] = line[1].strip()
    INF = 10**18
    # Precompute suffix lens: lens_suf[i][ch] = length of expansion of ch after ops i+1..n
    lens_suf = [[0]*26 for _ in range(n+1)]
    # after all ops, each char is itself
    for j in range(26):
        lens_suf[n][j] = 1
    # build backwards
    for i in range(n, 0, -1):
        # start from lens_suf[i]
        cur = lens_suf[i-1]
        prev = lens_suf[i]
        # copy
        for j in range(26): cur[j] = prev[j]
        # apply op i: replace c -> s
        c = ops_c[i]
        tot = 0
        for ch in ops_s[i]:
            tot += prev[ord(ch)-97]
            if tot >= INF:
                tot = INF
                break
        cur[c] = tot
    sys.setrecursionlimit(10000000)
    res = []
    # dfs forward from depth i, expand ch through ops i+1..n
    def dfs(ch, i, L, R):  # L,R inclusive
        if L > R: return
        if i == n:
            # no more ops, single char
            if L <= 1 <= R:
                res.append(chr(ch+97))
            return
        # length of full expansion
        # skip if ch not replaced in op i+1
        c = ops_c[i+1]
        if ch != c:
            dfs(ch, i+1, L, R)
        else:
            # expand via s
            sum_prev = 0
            for c0 in ops_s[i+1]:
                cj = ord(c0) - 97
                lj = lens_suf[i+1][cj]
                l_j = sum_prev + 1
                r_j = sum_prev + lj
                if r_j >= L and l_j <= R:
                    innerL = max(1, L - sum_prev)
                    innerR = min(lj, R - sum_prev)
                    dfs(cj, i+1, innerL, innerR)
                sum_prev = r_j
                if sum_prev > R:
                    break
    # start from initial 'a' at op 0
    dfs(0, 0, l, r)
    sys.stdout.write(''.join(res))

if __name__ == '__main__':
    main()
