#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    a = [int(next(it)) for _ in range(n)]
    q = int(next(it))
    qs = []  # list of (i, j)
    js = []
    for _ in range(q):
        idx = int(next(it)) - 1
        j = int(next(it))
        qs.append((idx, j))
        js.append(j)
    # coord compress values in a and js
    vals = sorted(set(a) | set(js))
    m = len(vals)
    comp = {v: i+1 for i, v in enumerate(vals)}  # 1-indexed
    # BITs
    class BIT:
        __slots__ = ('n','t')
        def __init__(self, n): self.n = n; self.t = [0]*(n+1)
        def add(self, i, v):
            while i <= self.n:
                self.t[i] += v
                i += i & -i
        def sum(self, i):
            s = 0
            while i > 0:
                s += self.t[i]
                i -= i & -i
            return s
    bit_cnt = BIT(m)
    bit_sum = BIT(m)
    for v in a:
        idx = comp[v]
        bit_cnt.add(idx, 1)
        bit_sum.add(idx, v)
    total_sum = sum(a)
    # compute T_old by sorting
    b = sorted(a)
    T0 = 0
    # use 1-indexed positions
    for i, v in enumerate(b, start=1):
        T0 += v * i
    out = []
    for idx, j in qs:
        v = a[idx]
        if v == j:
            out.append(str(T0))
            continue
        iv = comp[v]
        ij = comp[j]
        # removal
        cnt_less_v = bit_cnt.sum(iv-1)
        cnt_eq_v = bit_cnt.sum(iv) - cnt_less_v
        sum_le_v = bit_sum.sum(iv)
        sum_gt_v = total_sum - sum_le_v
        delta_rem = - (v * (cnt_less_v + cnt_eq_v) + sum_gt_v)
        # insertion, after removal
        # original counts
        cnt_less_j0 = bit_cnt.sum(ij-1)
        cnt_eq_j0 = bit_cnt.sum(ij) - cnt_less_j0
        sum_le_j0 = bit_sum.sum(ij)
        sum_gt_j0 = total_sum - sum_le_j0
        # adjust for removal of v
        if v < j:
            cnt_less_j = cnt_less_j0 - 1
        else:
            cnt_less_j = cnt_less_j0
        if v == j:
            cnt_eq_j = cnt_eq_j0 - 1
        else:
            cnt_eq_j = cnt_eq_j0
        if v > j:
            sum_gt_j = sum_gt_j0 - v
        else:
            sum_gt_j = sum_gt_j0
        delta_ins = j * (cnt_less_j + cnt_eq_j + 1) + sum_gt_j
        out.append(str(T0 + delta_rem + delta_ins))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
