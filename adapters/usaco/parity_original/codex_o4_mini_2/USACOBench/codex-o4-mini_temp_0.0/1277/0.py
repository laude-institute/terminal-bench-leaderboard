#!/usr/bin/env python3
"""
Compute minimum operations to transform strings of 'M' and 'O' into 'MOO'
using only end deletions and end flips (M<->O).
"""
import sys

def min_operations_to_moo(s: str) -> int:
    n = len(s)
    # Cannot form 'MOO' if less than length 3
    if n < 3:
        return -1
    best = None
    # Consider every substring of length 3
    for i in range(n - 2):
        # Middle character must match 'O' (cannot flip middle)
        if s[i + 1] != 'O':
            continue
        # Deletes needed to isolate substring: remove all others
        deletes = i + (n - 3 - i)
        # Flips needed at ends if characters differ
        flips = (s[i] != 'M') + (s[i + 2] != 'O')
        ops = deletes + flips
        if best is None or ops < best:
            best = ops
    return best if best is not None else -1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    q = int(data[0])
    outputs = []
    idx = 1
    for _ in range(q):
        s = data[idx]
        idx += 1
        outputs.append(str(min_operations_to_moo(s)))
    sys.stdout.write("\n".join(outputs))

if __name__ == '__main__':
    main()
