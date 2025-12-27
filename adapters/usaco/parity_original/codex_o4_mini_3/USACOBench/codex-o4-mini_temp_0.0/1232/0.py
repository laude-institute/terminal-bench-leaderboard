#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    s = data[0]
    n = len(s)
    Q = int(data[1])
    lr = list(map(int, data[2:]))

    # State indices: 0=empty, 1=C, 2=O, 3=W
    # Precomputed transition for each single character
    # fX[x] = new state after reducing [state x] + [letter X]
    fC = [1, 0, 3, 2]
    fO = [2, 3, 0, 1]
    fW = [3, 2, 1, 0]
    fmap = {'C': fC, 'O': fO, 'W': fW}

    # Segment tree size (power of two)
    size = 1
    while size < n:
        size <<= 1
    # Initialize tree with identity mapping
    seg = [[i for i in range(4)] for _ in range(2 * size)]

    # Set leaves based on input string
    for i, ch in enumerate(s):
        seg[size + i] = fmap[ch][:]

    # Compose two mappings: fB after fA
    def compose(fB, fA):
        return [fB[fA[i]] for i in range(4)]

    # Build internal nodes
    for i in range(size - 1, 0, -1):
        left = seg[2 * i]
        right = seg[2 * i + 1]
        seg[i] = compose(right, left)

    # Process queries
    out = []
    for qi in range(Q):
        l = lr[2 * qi] - 1
        r = lr[2 * qi + 1]  # exclusive end at r
        l += size
        r += size
        # Initialize accumulators as identity
        left_res = [i for i in range(4)]
        right_res = [i for i in range(4)]
        # Range query [l, r)
        while l < r:
            if l & 1:
                left_res = compose(seg[l], left_res)
                l += 1
            if r & 1:
                r -= 1
                right_res = compose(right_res, seg[r])
            l //= 2
            r //= 2
        total = compose(right_res, left_res)
        # Check if reduced result from empty state is 'C' (state 1)
        out.append('Y' if total[0] == 1 else 'N')

    sys.stdout.write(''.join(out))


if __name__ == '__main__':
    main()
