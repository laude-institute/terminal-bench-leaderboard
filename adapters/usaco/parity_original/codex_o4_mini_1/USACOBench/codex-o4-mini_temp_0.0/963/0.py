#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    K, N = map(int, data[:2])
    idx = 2
    sessions = []
    for _ in range(K):
        sessions.append(list(map(int, data[idx:idx+N])))
        idx += N
    # Precompute positions
    pos = [dict() for _ in range(K)]
    for k in range(K):
        for rank, cow in enumerate(sessions[k]):
            pos[k][cow] = rank
    count = 0
    # Check each pair
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            i_better = all(pos[k][i] < pos[k][j] for k in range(K))
            j_better = all(pos[k][j] < pos[k][i] for k in range(K))
            if i_better or j_better:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
