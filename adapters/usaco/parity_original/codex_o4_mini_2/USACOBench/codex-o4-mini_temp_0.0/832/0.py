#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    # Read hierarchy order
    hierarchy = [int(next(it)) for _ in range(M)]
    # Read fixed position constraints
    fixed = {}
    pos_used = {}
    for _ in range(K):
        c = int(next(it)); p = int(next(it))
        fixed[c] = p
        pos_used[p] = c

    # If cow 1 has a fixed position, that's the answer
    if 1 in fixed:
        print(fixed[1])
        return

    # Try each possible position for cow 1
    for p1 in range(1, N+1):
        # Skip if position already taken
        if p1 in pos_used:
            continue
        # Set cow 1 to p1
        cow_to_pos = dict(fixed)
        cow_to_pos[1] = p1
        # Build order array, 0=empty
        order = [0] * (N + 1)
        for c, pos in cow_to_pos.items():
            order[pos] = c

        cur = 1
        ok = True
        # Place hierarchy cows greedily
        for c in hierarchy:
            if c in cow_to_pos:
                p = cow_to_pos[c]
                if p < cur:
                    ok = False
                    break
                cur = p + 1
            else:
                # find next empty slot
                while cur <= N and order[cur] != 0:
                    cur += 1
                if cur > N:
                    ok = False
                    break
                order[cur] = c
                cur += 1
        if ok:
            print(p1)
            return

if __name__ == '__main__':
    main()
