#!/usr/bin/env python3
"""
Perform two fixed subarray reversals K times on a list of N cows.
Compute the resulting permutation via cycle decomposition.
"""
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    # zero-based indices for reversals
    A1 -= 1; A2 -= 1; B1 -= 1; B2 -= 1

    # Build one-step permutation P: position i -> position after one full iteration
    P = list(range(N))
    # First reversal
    P[A1:A2+1] = reversed(P[A1:A2+1])
    # Second reversal
    P[B1:B2+1] = reversed(P[B1:B2+1])

    # Compute P^K via cycle decomposition
    final_pos = [-1] * N
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            # build cycle starting at i
            cycle = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = P[cur]
            length = len(cycle)
            # place each element after K applications
            for idx, pos in enumerate(cycle):
                new_idx = (idx + K) % length
                final_pos[cycle[new_idx]] = pos

    # result[position] = label of cow ending here
    result = [0] * N
    for end_pos, start_pos in enumerate(final_pos):
        result[end_pos] = start_pos + 1

    # output
    print("\n".join(map(str, result)))

if __name__ == '__main__':
    main()
