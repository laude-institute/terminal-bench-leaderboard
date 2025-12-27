#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    swaps = [tuple(map(int, input().split())) for _ in range(K)]

    # Initialize positions and visited sets
    # pos_of_cow[i]: current position of cow i
    # cow_at_pos[p]: which cow is at position p
    pos_of_cow = list(range(N+1))
    cow_at_pos = list(range(N+1))
    visited = [set() for _ in range(N+1)]
    for i in range(1, N+1):
        visited[i].add(i)

    # Simulate one full sequence of swaps
    for a, b in swaps:
        c1 = cow_at_pos[a]
        c2 = cow_at_pos[b]
        # record visited positions
        visited[c1].add(b)
        visited[c2].add(a)
        # swap cows
        cow_at_pos[a], cow_at_pos[b] = c2, c1
        pos_of_cow[c1] = b
        pos_of_cow[c2] = a

    # Build permutation mapping after one sequence
    P = pos_of_cow
    ans = [0] * (N+1)
    seen = [False] * (N+1)

    # Process each cycle in the permutation
    for i in range(1, N+1):
        if not seen[i]:
            cycle = []
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cycle.append(cur)
                cur = P[cur]
            # Union visited positions for all cows in this cycle
            union_set = set()
            for c in cycle:
                union_set |= visited[c]
            count = len(union_set)
            for c in cycle:
                ans[c] = count

    # Output results
    out = sys.stdout.write
    for i in range(1, N+1):
        out(str(ans[i]) + "\n")

if __name__ == "__main__":
    main()
