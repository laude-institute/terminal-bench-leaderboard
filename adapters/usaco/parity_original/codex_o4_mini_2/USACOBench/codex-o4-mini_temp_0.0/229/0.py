#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    B = list(map(int, data[2:]))
    freq = {}
    distinct = 0
    l = 0
    ans = 0
    # Sliding window with at most K+1 distinct breeds
    for r in range(N):
        b = B[r]
        freq[b] = freq.get(b, 0) + 1
        if freq[b] == 1:
            distinct += 1
        # Shrink window if too many distinct breeds
        while distinct > K + 1:
            bl = B[l]
            freq[bl] -= 1
            if freq[bl] == 0:
                distinct -= 1
            l += 1
        # After removal of other breeds, contiguous block of b has size freq[b]
        ans = max(ans, freq[b])
    print(ans)

if __name__ == '__main__':
    main()
