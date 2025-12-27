#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n, L = map(int, data[:2])
    citations = list(map(int, data[2:2+n]))
    # Build frequency array up to max(n, max(citations))+2
    max_c = max(citations) if citations else 0
    size = max(max_c, n) + 2
    freq = [0] * size
    for c in citations:
        freq[c] += 1
    # Build suffix sums: suff[i] = number of papers with >= i citations
    suff = [0] * (size + 1)
    suff[size-1] = freq[size-1]
    for i in range(size-2, -1, -1):
        suff[i] = freq[i] + suff[i+1]

    def can_achieve(h):
        if h == 0:
            return True
        # papers with >= h citations already
        G = suff[h] if h < len(suff) else 0
        # papers with exactly h-1 citations
        B = freq[h-1] if h-1 < len(freq) else 0
        needed = h - G
        if needed <= 0:
            return True
        return needed <= L and needed <= B

    # Binary search maximum h in [0..n]
    low, high = 0, n
    while low < high:
        mid = (low + high + 1) // 2
        if can_achieve(mid):
            low = mid
        else:
            high = mid - 1
    print(low)

if __name__ == '__main__':
    main()
