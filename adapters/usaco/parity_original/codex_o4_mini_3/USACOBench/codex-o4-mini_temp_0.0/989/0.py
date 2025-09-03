#!/usr/bin/env python3
"""
Compute minimal time to run K meters with end speed ≤ X.
"""
import sys

def max_dist(T, X):
    # Maximum distance in T seconds with final speed ≤ X
    if T <= X:
        return T * (T + 1) // 2
    # Peak speed m reached
    m = (T + X) // 2
    # Plateau duration
    p = T - 2 * m + X
    # Distance during acceleration: speeds 1..m
    acc = m * (m + 1) // 2
    # Distance during plateau: p times at speed m
    plat = p * m
    # Distance during deceleration: speeds m-1 down to X
    dec = (m + X - 1) * (m - X) // 2
    return acc + plat + dec

def min_time(K, X):
    lo, hi = 0, 2 * K
    while lo < hi:
        mid = (lo + hi) // 2
        if max_dist(mid, X) >= K:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    data = sys.stdin.read().split()
    K = int(data[0])
    N = int(data[1])
    xs = list(map(int, data[2:2 + N]))
    result = []
    for X in xs:
        result.append(str(min_time(K, X)))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
