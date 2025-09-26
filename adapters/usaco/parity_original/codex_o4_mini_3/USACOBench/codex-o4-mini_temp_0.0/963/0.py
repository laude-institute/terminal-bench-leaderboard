#!/usr/bin/env python3
import sys

def main():
    # Read number of sessions (K) and number of cows (N)
    K, N = map(int, sys.stdin.readline().split())
    # Read rankings for each session
    sessions = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

    # Build position maps: pos[s][cow] = rank index of cow in session s
    pos = []
    for sess in sessions:
        mapping = {}
        for idx, cow in enumerate(sess):
            mapping[cow] = idx
        pos.append(mapping)

    # Count consistent pairs
    count = 0
    # Iterate over all pairs of distinct cows (i, j)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            # Check if i is always ahead of j in all sessions
            i_ahead = all(pos[s][i] < pos[s][j] for s in range(K))
            # Check if j is always ahead of i in all sessions
            j_ahead = all(pos[s][j] < pos[s][i] for s in range(K))
            if i_ahead or j_ahead:
                count += 1

    # Output the result
    print(count)

if __name__ == "__main__":
    main()
