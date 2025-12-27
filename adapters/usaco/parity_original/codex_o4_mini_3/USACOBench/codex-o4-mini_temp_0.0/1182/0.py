#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10000)
from functools import lru_cache

def reduce_cost(a, b):
    """
    When a >= b, compute minimum operations to reduce a to b
    using /2 when even or +1 when odd, then final +1 operations.
    """
    cost = 0
    while a > b:
        if a % 2 == 0:
            a //= 2
        else:
            a += 1
        cost += 1
    # now a <= b, adjust by +1 operations
    cost += (b - a)
    return cost

@lru_cache(maxsize=None)
def solve(a, b):
    # If starting >= target, use greedy reduction
    if a >= b:
        return reduce_cost(a, b)
    # Option 1: only add operations
    best = b - a
    # Option 2: add i1 times, then multiply, then solve recursively
    # target half floor
    i1 = b // 2 - a
    if i1 < 0:
        i1 = 0
    newa = (a + i1) * 2
    best = min(best, i1 + 1 + solve(newa, b))
    # Option 3: add i2 times based on ceil half
    i2 = (b + 1) // 2 - a
    if i2 < 0:
        i2 = 0
    newa = (a + i2) * 2
    best = min(best, i2 + 1 + solve(newa, b))
    return best

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    out = []
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        out.append(str(solve(a, b)))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
