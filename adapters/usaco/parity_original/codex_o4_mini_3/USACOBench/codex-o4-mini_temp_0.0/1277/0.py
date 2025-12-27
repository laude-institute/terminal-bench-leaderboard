#!/usr/bin/env python3
import sys

def min_operations_to_moo(s: str) -> int:
    n = len(s)
    # Cannot form "MOO" if less than length 3
    if n < 3:
        return -1
    best = float('inf')
    # Try all substrings of length 3 by deleting from ends
    for i in range(0, n - 3 + 1):
        t = s[i:i+3]
        # middle must be 'O'
        if t[1] != 'O':
            continue
        # deletions: i from front, (n-3-i) from back
        cost = i + (n - 3 - i)
        # toggles for first and last
        if t[0] != 'M':
            cost += 1
        if t[2] != 'O':
            cost += 1
        best = min(best, cost)
    return best if best != float('inf') else -1

def main():
    data = sys.stdin.read().strip().split()
    q = int(data[0])
    idx = 1
    out = []
    for _ in range(q):
        s = data[idx]
        idx += 1
        out.append(str(min_operations_to_moo(s)))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
