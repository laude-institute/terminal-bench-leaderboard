#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    breeds = [int(next(it)) for _ in range(n)]

    # Compute original maximum block without removal
    ans = 0
    prev = None
    count = 0
    for b in breeds:
        if b == prev:
            count += 1
        else:
            prev = b
            count = 1
        if count > ans:
            ans = count

    # Try removing each breed ID and compute max block
    unique = set(breeds)
    for rem in unique:
        prev = None
        count = 0
        cur_max = 0
        for b in breeds:
            if b == rem:
                continue
            if b == prev:
                count += 1
            else:
                prev = b
                count = 1
            if count > cur_max:
                cur_max = count
        if cur_max > ans:
            ans = cur_max

    print(ans)

if __name__ == '__main__':
    main()
