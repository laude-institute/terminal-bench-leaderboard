#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    f = list(map(int, input().split()))
    # Sort tiles by snow depth descending
    tiles = sorted([(f_val, idx) for idx, f_val in enumerate(f)], key=lambda x: -x[0])
    # Read boots and keep original indices
    boots = []  # (s, d, original_index)
    for i in range(B):
        s, d = map(int, input().split())
        boots.append((s, d, i))
    # Sort boots by max snow depth descending
    boots_sorted = sorted(boots, key=lambda x: -x[0])

    # Doubly linked list over positions 0..N-1
    prev = [i - 1 for i in range(N)]
    next = [i + 1 for i in range(N)]
    # Track maximum gap between usable tiles
    max_gap = 1
    res = [0] * B
    ti = 0
    # Process boots in descending s
    for s, d, idx in boots_sorted:
        # Remove all tiles with f > s
        while ti < N and tiles[ti][0] > s:
            pos = tiles[ti][1]
            l = prev[pos]
            r = next[pos]
            # unlink pos
            next[l] = r
            prev[r] = l
            # update maximum gap
            gap = r - l
            if gap > max_gap:
                max_gap = gap
            ti += 1
        # If max gap <= d, boot is usable
        res[idx] = 1 if max_gap <= d else 0

    # Output results in original order
    out = '\n'.join(str(x) for x in res)
    sys.stdout.write(out)

if __name__ == '__main__':
    main()
