#!/usr/bin/env python3
import sys
def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    W = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            W[i][j] = int(next(it))
    rem = [(0,0)]*(N*N)
    for idx in range(N*N):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        rem[idx] = (a, b)
    INF = 10**30
    # dp_pref[l][u]: min weight from 1 to u in exactly l edges
    # dp_rev[l][u]: min weight from u to N in exactly l edges
    dp_pref = [[INF]*N for _ in range(K+1)]
    dp_rev = [[INF]*N for _ in range(K+1)]
    dp_pref[0][0] = 0
    dp_rev[0][N-1] = 0
    total = N*N
    ans = [-1] * (total+1)
    ans_value = INF
    # reverse process: add edges in reverse removal order
    for j in range(1, total+1):
        # addition index
        a, b = rem[total - j]
        w = W[a][b]
        # update prefix dp
        for l in range(1, K+1):
            val = dp_pref[l-1][a] + w
            if val < dp_pref[l][b]: dp_pref[l][b] = val
        # update suffix dp
        for l in range(1, K+1):
            val = w + dp_rev[l-1][b]
            if val < dp_rev[l][a]: dp_rev[l][a] = val
        # check new paths using this edge at any position
        for t in range(1, K+1):
            pre = dp_pref[t-1][a]
            suf = dp_rev[K-t][b]
            if pre < INF and suf < INF:
                cand = pre + w + suf
                if cand < ans_value:
                    ans_value = cand
        idx = total - j
        ans[idx] = ans_value if ans_value < INF else -1
    # output answers after each removal (1..total)
    out = []
    for i in range(1, total+1):
        out.append(str(ans[i]))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
