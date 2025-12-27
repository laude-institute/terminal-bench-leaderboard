#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    idx = 2
    cows = []
    for _ in range(N):
        s, t, c = map(int, data[idx:idx+3])
        idx += 3
        cows.append((s, t, c))
    acs = []
    for _ in range(M):
        a, b, p, m = map(int, data[idx:idx+4])
        idx += 4
        acs.append((a, b, p, m))
    best = float('inf')
    # Try all subsets of air conditioners
    for mask in range(1 << M):
        cost = 0
        for i in range(M):
            if (mask >> i) & 1:
                cost += acs[i][3]
        if cost >= best:
            continue
        # Compute cooling effect at each stall
        temp = [0] * 101
        for i in range(M):
            if (mask >> i) & 1:
                a, b, p, _ = acs[i]
                for j in range(a, b + 1):
                    temp[j] += p
        # Check if all cows are satisfied
        ok = True
        for s, t, c in cows:
            for j in range(s, t + 1):
                if temp[j] < c:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = cost
    print(best)

if __name__ == '__main__':
    main()
