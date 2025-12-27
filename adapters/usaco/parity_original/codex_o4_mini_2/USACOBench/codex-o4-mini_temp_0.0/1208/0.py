#!/usr/bin/env python3
import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n+1)
    def add(self, i, v):
        # i: 1-indexed
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def sum(self, i):
        # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    def select(self, k):
        # smallest i such that sum(i) >= k
        i = 0
        bit = 1 << (self.n.bit_length())
        while bit:
            j = i + bit
            if j <= self.n and self.fw[j] < k:
                i = j
                k -= self.fw[j]
            bit >>= 1
        return i + 1

class SegTree:
    def __init__(self, data, default, func):
        # data 1-indexed
        self.n = len(data) - 1
        self.default = default
        self.func = func
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [default] * (2*size)
        for i in range(1, self.n+1):
            self.tree[size+i-1] = data[i]
        for i in range(size-1, 0, -1):
            self.tree[i] = func(self.tree[2*i], self.tree[2*i+1])
    def update(self, i, v):
        # set data[i] = v
        pos = self.size + i - 1
        self.tree[pos] = v
        pos //= 2
        while pos:
            self.tree[pos] = self.func(self.tree[2*pos], self.tree[2*pos+1])
            pos //= 2
    def query(self, l, r):  # inclusive
        res = self.default
        l = l + self.size - 1
        r = r + self.size - 1
        while l <= r:
            if (l & 1) == 1:
                res = self.func(res, self.tree[l]); l += 1
            if (r & 1) == 0:
                res = self.func(res, self.tree[r]); r -= 1
            l //= 2; r //= 2
        return res

def solve_case(M, N, K, f):
    # prepare per-folder lists of positions
    pos_lists = [[] for _ in range(M+1)]
    for i, fi in enumerate(f, start=1):
        pos_lists[fi].append(i)
    # pointers to head in each list
    ptr = [0] * (M+1)
    INF = N+1
    # initial min pos per folder
    init = [INF] * (M+1)
    for j in range(1, M+1):
        if ptr[j] < len(pos_lists[j]):
            init[j] = pos_lists[j][ptr[j]]
    # build structures
    bit = Fenwick(N)
    for i in range(1, N+1): bit.add(i, 1)
    seg = SegTree(init, INF, min)
    unread = N
    email_start = 0  # 0-indexed among unread
    folder_start = 1
    done = 0
    # process all
    while done < N:
        # compute window on emails
        if unread > K:
            max_start = unread - K
            if email_start > max_start:
                email_start = max_start
            start_un = email_start
            end_un = start_un + K - 1
        else:
            start_un = 0
            end_un = unread - 1
        # find original indices of window
        left_orig = bit.select(start_un+1)
        right_orig = bit.select(end_un+1)
        # query folder window
        lowF = folder_start
        highF = folder_start + K - 1
        if highF > M:
            highF = M
        minpos = seg.query(lowF, highF)
        if minpos == INF:
            # no candidate folder, scroll folder or email
            if highF < M:
                folder_start += 1
                continue
            # try scroll email
            if unread > K and email_start < unread - K:
                email_start += 1
                continue
            return False
        # have a folder candidate at original pos minpos
        if minpos < left_orig:
            # above view, scroll email
            if unread > K and email_start < unread - K:
                email_start += 1
                continue
            return False
        if minpos > right_orig:
            # below view, scroll email to include it
            # desired start = rank(minpos)-1
            rank = bit.sum(minpos)
            target = rank - 1
            if unread > K:
                email_start = target if target <= unread - K else unread - K
            else:
                email_start = 0
            continue
        # process email at minpos
        bit.add(minpos, -1)
        unread -= 1
        # update folder list and segtree
        # find folder fidx
        fidx = f[minpos-1]
        ptr[fidx] += 1
        if ptr[fidx] < len(pos_lists[fidx]):
            seg.update(fidx, pos_lists[fidx][ptr[fidx]])
        else:
            seg.update(fidx, INF)
        done += 1
        # adjust email_start if at bottom
        if unread >= K and start_un == (unread+1) - (K+1):
            # old start_un == old_unread-K
            email_start = unread - K
        # continue
    return True

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        M = int(next(it)); N = int(next(it)); K = int(next(it))
        f = [int(next(it)) for _ in range(N)]
        res = solve_case(M, N, K, f)
        out.append("YES" if res else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
