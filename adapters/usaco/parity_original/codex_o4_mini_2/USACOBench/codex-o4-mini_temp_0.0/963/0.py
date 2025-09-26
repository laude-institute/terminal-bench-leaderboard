#!/usr/bin/env python3
"""
Reads K practice sessions of N cows' rankings,
and counts unordered pairs of cows consistent across all sessions.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    K, N = map(int, data[:2])
    idx = 2
    # pos[s][cow] = position of cow in session s
    pos = []
    for _ in range(K):
        ranking = list(map(int, data[idx:idx+N]))
        idx += N
        p = {cow: i for i, cow in enumerate(ranking)}
        pos.append(p)
    count = 0
    # Check each unordered pair
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            # Check if i always above j or j always above i
            better_i = all(p[i] < p[j] for p in pos)
            better_j = all(p[j] < p[i] for p in pos)
            if better_i or better_j:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
