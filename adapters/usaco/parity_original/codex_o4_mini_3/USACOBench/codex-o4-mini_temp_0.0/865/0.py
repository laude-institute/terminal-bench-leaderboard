#!/usr/bin/env python3
import sys
def main():
    import sys
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    p = [int(next(it)) for _ in range(N)]
    # Fenwick tree for (maxlen, count)
    INF = 10**18
    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.f = [(0, 0)] * (n+1)
        def update(self, i, length, count):
            while i <= self.n:
                prev_len, prev_cnt = self.f[i]
                if length > prev_len:
                    self.f[i] = (length, count)
                elif length == prev_len:
                    nc = prev_cnt + count
                    if nc > INF: nc = INF
                    self.f[i] = (length, nc)
                i += i & -i
        def query(self, i):
            best_len, best_cnt = 0, 0
            while i > 0:
                l, c = self.f[i]
                if l > best_len:
                    best_len, best_cnt = l, c
                elif l == best_len:
                    best_cnt += c
                    if best_cnt > INF: best_cnt = INF
                i -= i & -i
            return best_len, best_cnt
    # dp left
    ft = Fenwick(N)
    dpleft = [0]*N
    cntL = [0]*N
    for i in range(N):
        v = p[i]
        l, c = ft.query(v-1)
        if l == 0:
            l, c = 1, 1
        else:
            l += 1
        dpleft[i] = l
        cntL[i] = c
        ft.update(v, l, c)
    # dp right
    ft2 = Fenwick(N)
    dpR = [0]*N
    cntR = [0]*N
    for i in range(N-1, -1, -1):
        # consider larger values: map to inverted index
        v = p[i]
        idx = N - v + 1
        l, c = ft2.query(idx-1)
        if l == 0:
            l, c = 1, 1
        else:
            l += 1
        dpR[i] = l
        cntR[i] = c
        ft2.update(idx, l, c)
    # compute LIS length
    L = max(dpleft)
    # collect candidates per layer
    layers = [[] for _ in range(L+1)]
    for i in range(N):
        if dpleft[i] + dpR[i] - 1 == L:
            layers[dpleft[i]].append(i)
    # sort each layer by value
    for d in range(1, L+1):
        layers[d].sort(key=lambda i: p[i])
    # total number of LIS = sum cntR at layer 1
    M = 0
    for i in layers[1]:
        M = min(INF, M + cntR[i])
    # target index in LIS list
    Y = M - K + 1
    # build LIS sequence positions
    seq = []
    prev_pos = -1
    for d in range(1, L+1):
        total = 0
        for i in layers[d]:
            if i <= prev_pos: continue
            c = cntR[i]
            if total + c >= Y:
                seq.append(i)
                prev_pos = i
                Y -= total
                break
            total += c
        else:
            # should not happen
            pass
    # seq holds positions of LIS
    T = set(p[i] for i in seq)
    # minimal cover S = all IDs not in T
    S = [i for i in range(1, N+1) if i not in T]
    # output
    out = []
    out.append(str(len(S)))
    for x in S:
        out.append(str(x))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
