#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N = int(input())
    # Read and sort segments by left endpoint
    segs = [tuple(map(int, input().split())) for _ in range(N)]
    segs.sort(key=lambda x: x[0])

    # BIT for counting previous segments by right endpoint
    max_coord = 2 * N
    size = max_coord + 5
    bit = [0] * size

    def bit_add(i, v):
        while i < size:
            bit[i] += v
            i += i & -i

    def bit_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Precompute powers of two mod MOD
    p2 = [1] * (N + 1)
    for i in range(1, N + 1):
        p2[i] = (p2[i - 1] * 2) % MOD

    ans = 0
    # Process each segment in sorted order
    for idx, (l, r) in enumerate(segs):
        # Count of previous segments with right < l
        c_lt = bit_sum(l - 1)
        # Number of previous segments = idx
        # Number overlapping on left = idx - c_lt
        # Contribution exponent = N-1 - (idx - c_lt)
        exp = N - 1 - (idx - c_lt)
        ans = (ans + p2[exp]) % MOD
        # Mark this segment's right endpoint
        bit_add(r, 1)

    print(ans)


if __name__ == '__main__':
    main()
