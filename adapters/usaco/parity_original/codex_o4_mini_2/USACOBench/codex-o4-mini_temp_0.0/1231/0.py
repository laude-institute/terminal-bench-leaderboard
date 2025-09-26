#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    s = data.readline().strip()
    t = data.readline().strip()
    # map letters a-r to 0-17
    def to_id(c): return ord(c) - ord('a')
    s_ids = [to_id(c) for c in s]
    t_ids = [to_id(c) for c in t]
    # count per letter
    L = 18
    count_s = [0]*L
    count_t = [0]*L
    for x in s_ids: count_s[x] += 1
    for x in t_ids: count_t[x] += 1
    # mask of letters with equal counts
    ok_counts = 0
    for c in range(L):
        if count_s[c] == count_t[c]: ok_counts |= 1 << c
    # equal pair projections
    eq = [[False]*L for _ in range(L)]
    # precompute projections for each pair
    for c in range(L):
        for d in range(c+1, L):
            # build projections
            proj_s = [x for x in s_ids if x == c or x == d]
            proj_t = [x for x in t_ids if x == c or x == d]
            if proj_s == proj_t:
                eq[c][d] = eq[d][c] = True
    # ok pairs mask per letter
    ok_pairs = [0]*L
    for c in range(L):
        m = 0
        for d in range(L):
            if d != c and eq[c][d]: m |= 1 << d
        ok_pairs[c] = m
    # process queries
    Q = int(data.readline().strip())
    out = []
    for _ in range(Q):
        line = data.readline().strip()
        mask = 0
        for ch in line:
            mask |= 1 << to_id(ch)
        # check counts
        if mask & ~ok_counts:
            out.append('N')
            continue
        # check pair orders
        bad = False
        m = mask
        while m:
            c = (m & -m).bit_length() - 1
            m &= m - 1
            # other letters in subset
            others = mask ^ (1 << c)
            if others & ~ok_pairs[c]:
                bad = True
                break
        out.append('N' if bad else 'Y')
    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    main()
