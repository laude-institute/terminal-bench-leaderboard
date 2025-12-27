#!/usr/bin/env python3
import sys

def max_dist(T, X):
    # Maximum distance in T seconds ending at speed <= X
    if T <= X:
        return T * (T + 1) // 2
    # Peak speed
    m = (T + X) // 2
    # Distance accelerating 0->m
    d1 = m * (m + 1) // 2
    # Distance decelerating m->X (speeds m-1 down to X)
    d2 = (m + X - 1) * (m - X) // 2
    # Remaining flat time at speed m
    used = 2 * m - X
    d3 = m * (T - used)
    return d1 + d2 + d3

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
    K, N = map(int, data[:2])
    Xs = map(int, data[2:])
    out = []
    for X in Xs:
        out.append(str(min_time(K, X)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
