#!/usr/bin/env python3
import sys

INF = 10**9

class BIT:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n+1)
    def add(self, i, v):
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.data = [INF] * (2*self.size)
        for i in range(self.n):
            self.data[self.size + i] = arr[i]
        for i in range(self.size-1, 0, -1):
            self.data[i] = min(self.data[2*i], self.data[2*i+1])
    def update(self, i, v):
        # set arr[i] = v
        i += self.size
        self.data[i] = v
        i //= 2
        while i:
            self.data[i] = min(self.data[2*i], self.data[2*i+1])
            i //= 2
    def query(self, l, r):  # inclusive l..r
        res = INF
        l += self.size; r += self.size
        while l <= r:
            if (l & 1) == 1:
                res = min(res, self.data[l]); l += 1
            if (r & 1) == 0:
                res = min(res, self.data[r]); r -= 1
            l //= 2; r //= 2
        return res

def can_file(M, N, K, f):
    # prepare per-folder queues of positions
    folder_q = [[] for _ in range(M+1)]
    for i, fi in enumerate(f, start=1):
        folder_q[fi].append(i)
    # initial min positions array
    init = []
    for fi in range(1, M+1):
        init.append(folder_q[fi][0] if folder_q[fi] else INF)
    st = SegTree(init)
    bit = BIT(N)
    for i in range(1, N+1): bit.add(i, 1)
    total = N
    folder_start = 1
    email_start = 1
    # main loop
    while total > 0:
        # folder window
        max_fstart = max(1, M - K + 1)
        fL = folder_start
        fR = min(M, folder_start + K - 1)
        # candidate earliest email
        p = st.query(fL-1, fR-1)
        # if none, try scroll
        if p >= INF:
            max_estart = max(1, total - K + 1)
            if email_start < max_estart:
                email_start += 1
                continue
            if folder_start < max_fstart:
                folder_start += 1
                continue
            return False
        # get rank
        r = bit.sum(p)
        window_end = min(email_start + K - 1, total)
        # unreachable above window
        if r < email_start:
            return False
        # below window, scroll
        if r > window_end:
            max_estart = max(1, total - K + 1)
            if email_start < max_estart:
                email_start += 1
                continue
            if folder_start < max_fstart:
                folder_start += 1
                continue
            return False
        # file p
        bit.add(p, -1)
        total -= 1
        fi = f[p-1]
        # pop from folder queue
        folder_q[fi].pop(0)
        # update segtree
        nextp = folder_q[fi][0] if folder_q[fi] else INF
        st.update(fi-1, nextp)
        # adjust email_start if deletion from last window
        max_estart_new = max(1, total - K + 1)
        if email_start > max_estart_new:
            email_start = max_estart_new
    return True

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        M = int(next(it)); N = int(next(it)); K = int(next(it))
        f = [int(next(it)) for _ in range(N)]
        res = can_file(M, N, K, f)
        out.append("YES" if res else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
