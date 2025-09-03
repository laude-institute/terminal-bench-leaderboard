#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
def main():
    data = sys.stdin.read().split()
    N = int(data[0]); M = int(data[1])
    statements = []
    idx = 2
    for _ in range(M):
        x = int(data[idx]); y = int(data[idx+1]); t = data[idx+2]
        statements.append((x, y, t))
        idx += 3
    parent = list(range(N+1))
    parity = [0] * (N+1)
    def find(x):
        if parent[x] != x:
            orig = parent[x]
            parent[x] = find(orig)
            parity[x] ^= parity[orig]
        return parent[x]
    def union(x, y, p):
        rx = find(x); ry = find(y)
        if rx == ry:
            return (parity[x] ^ parity[y]) == p
        parent[ry] = rx
        parity[ry] = parity[x] ^ parity[y] ^ p
        return True
    def possible(k):
        for i in range(1, N+1):
            parent[i] = i; parity[i] = 0
        for i in range(k):
            x, y, t = statements[i]
            p = 0 if t == 'T' else 1
            if not union(x, y, p):
                return False
        return True
    lo, hi = 0, M
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if possible(mid):
            lo = mid
        else:
            hi = mid - 1
    print(lo)
if __name__ == "__main__":
    main()
