#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    s = data.readline().strip()
    t = data.readline().strip()
    n = len(s)
    # map letters 'a'-'r' to 0-17
    S = [ord(c) - 97 for c in s]
    T = [ord(c) - 97 for c in t]
    # counts per letter
    counts_s = [0] * 18
    counts_t = [0] * 18
    for c in S:
        counts_s[c] += 1
    for c in T:
        counts_t[c] += 1
    # single-letter equality
    equal_single = [counts_s[i] == counts_t[i] for i in range(18)]
    # pairwise equality for filtered sequences of two letters
    equal_pair = [[True] * 18 for _ in range(18)]
    # check for each letter pair i<j
    for i in range(18):
        for j in range(i+1, 18):
            p = q = 0
            ok = True
            while True:
                # advance p to next S[p] == i or j
                while p < n and S[p] != i and S[p] != j:
                    p += 1
                # advance q to next T[q] == i or j
                while q < n and T[q] != i and T[q] != j:
                    q += 1
                if p == n and q == n:
                    break
                if p == n or q == n or S[p] != T[q]:
                    ok = False
                    break
                p += 1
                q += 1
            equal_pair[i][j] = equal_pair[j][i] = ok
    # process queries
    out = []
    Q = int(data.readline().strip())
    for _ in range(Q):
        line = data.readline().strip()
        mask = [ord(c) - 97 for c in line]
        ans = 'Y'
        # check single letters
        for c in mask:
            if not equal_single[c]:
                ans = 'N'
                break
        # check pairs
        if ans == 'Y':
            m = len(mask)
            for u in range(m):
                cu = mask[u]
                for v in range(u+1, m):
                    cv = mask[v]
                    if not equal_pair[cu][cv]:
                        ans = 'N'
                        break
                if ans == 'N':
                    break
        out.append(ans)
    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    main()
