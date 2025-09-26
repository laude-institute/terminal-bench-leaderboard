#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    N, K = map(int, data[:2])
    tokens = data[2:]
    # Parse missing combinations
    missing = []
    idx = 0
    for _ in range(N):
        # skip 'Farmer John has no'
        idx += 4
        # read adjectives until 'cow.'
        comb = []
        while idx < len(tokens) and tokens[idx] != 'cow.':
            comb.append(tokens[idx])
            idx += 1
        # skip 'cow.'
        idx += 1
        missing.append(tuple(comb))
    if not missing:
        return
    D = len(missing[0])
    # collect adjectives per position
    pos_adjs = [set() for _ in range(D)]
    for comb in missing:
        for i, adj in enumerate(comb):
            pos_adjs[i].add(adj)
    # sort adjective lists
    adjs = [sorted(list(s)) for s in pos_adjs]
    # precompute suffix product of counts
    suffix = [1] * (D + 1)
    for i in range(D - 1, -1, -1):
        suffix[i] = suffix[i+1] * len(adjs[i])
    # find Kth cow
    result = []
    k = K
    for i in range(D):
        for a in adjs[i]:
            # count total combos if choose a here
            total = suffix[i+1]
            # count missing with this prefix
            prefix = tuple(result + [a])
            miss_cnt = 0
            for m in missing:
                if m[:i+1] == prefix:
                    miss_cnt += 1
            avail = total - miss_cnt
            if k > avail:
                k -= avail
            else:
                result.append(a)
                break
    # output result
    sys.stdout.write(" ".join(result))

if __name__ == '__main__':
    main()
