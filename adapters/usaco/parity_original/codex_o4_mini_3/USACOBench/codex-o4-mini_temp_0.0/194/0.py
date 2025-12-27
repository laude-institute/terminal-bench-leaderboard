#!/usr/bin/env python3
import sys

class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)
    def update(self, i, v):
        # maximize at position i
        while i <= self.n:
            if v > self.fw[i]: self.fw[i] = v
            i += i & -i
    def query(self, i):
        # max on [1..i]
        res = 0
        while i > 0:
            if self.fw[i] > res: res = self.fw[i]
            i -= i & -i
        return res

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    K = int(next(it))
    N = int(next(it))
    S = [next(it).strip() for _ in range(K)]

    # prefix sums for each string
    pref = [0] * K
    # Fenwicks to track last index of smaller prefix
    M = 2 * N + 5
    base = N + 2
    fw = [FenwickMax(M) for _ in range(K)]
    # init at position 0
    for k in range(K):
        fw[k].update(base, 0)

    # window of valid start positions
    left = 0
    window_left = 0
    # store past vectors
    vecs = [None] * (N + 1)
    start_vec = tuple([0] * K)
    vecs[0] = start_vec
    cnt = {start_vec: 1}
    result = 0

    # process positions 1..N
    for r in range(1, N + 1):
        # update prefix sums and compute last bad per string
        last_bad = 0
        for k in range(K):
            if S[k][r-1] == '(':
                pref[k] += 1
            else:
                pref[k] -= 1
            idx = pref[k] + base
            # last position with prefix < current
            lb = fw[k].query(idx - 1)
            if lb > last_bad:
                last_bad = lb
            # record this prefix position
            fw[k].update(idx, r)
        # advance left bound
        if last_bad > left:
            left = last_bad
        # evict old positions
        while window_left < left:
            v = vecs[window_left]
            cnt[v] -= 1
            window_left += 1
        # current vector
        cur = tuple(pref)
        vecs[r] = cur
        # count matching starts
        c = cnt.get(cur)
        if c:
            result += c
            cnt[cur] = c + 1
        else:
            cnt[cur] = 1

    # output result
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
