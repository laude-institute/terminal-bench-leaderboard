#!/usr/bin/env python3
import sys

def max_run(arr):
    """
    Return the maximum length of consecutive identical elements in arr.
    """
    best = 0
    cur = 0
    prev = None
    for x in arr:
        if x == prev:
            cur += 1
        else:
            cur = 1
            prev = x
        if cur > best:
            best = cur
    return best

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    breeds = list(map(int, data[1:1+n]))

    # Baseline: max run without removals
    best = max_run(breeds)

    # Try removing each breed and compute new max run
    for remove_id in set(breeds):
        filtered = [b for b in breeds if b != remove_id]
        best = max(best, max_run(filtered))

    print(best)

if __name__ == '__main__':
    main()
