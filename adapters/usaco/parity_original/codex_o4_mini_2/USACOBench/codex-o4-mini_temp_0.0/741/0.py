#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # map characters to integers
    char_map = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    # read genomes
    spot = [ [char_map[c] for c in input().strip()] for _ in range(N) ]
    plain = [ [char_map[c] for c in input().strip()] for _ in range(N) ]

    # rolling hash parameters
    base = 127
    mask = (1 << 64) - 1
    # precompute powers
    pw = [1] * (M + 1)
    for i in range(M):
        pw[i+1] = (pw[i] * base) & mask

    # compute prefix hashes for each genome
    def prefix_hash(seq):
        h = [0] * (M + 1)
        for i, v in enumerate(seq):
            h[i+1] = ((h[i] * base) + v) & mask
        return h

    spot_p = [prefix_hash(s) for s in spot]
    plain_p = [prefix_hash(p) for p in plain]

    # check if length L can distinguish
    def ok(L):
        for start in range(0, M - L + 1):
            seen = set()
            end = start + L
            # collect spotty hashes
            for h in spot_p:
                hs = (h[end] - (h[start] * pw[L] & mask)) & mask
                seen.add(hs)
            # check for conflict in plain cows
            conflict = False
            for h in plain_p:
                hs = (h[end] - (h[start] * pw[L] & mask)) & mask
                if hs in seen:
                    conflict = True
                    break
            if not conflict:
                return True
        return False

    # binary search for minimum length
    lo, hi = 1, M
    ans = M
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)

if __name__ == '__main__':
    main()
