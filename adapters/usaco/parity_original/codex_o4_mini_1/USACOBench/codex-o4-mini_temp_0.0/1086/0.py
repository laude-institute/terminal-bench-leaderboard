#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    swaps = [tuple(map(int, input().split())) for _ in range(K)]

    # Track positions visited by each cow during one round
    visited = [set() for _ in range(N + 1)]
    # Initialize cows at their starting positions
    cow_at_pos = list(range(N + 1))
    for cow in range(1, N + 1):
        visited[cow].add(cow)

    # Perform the K swaps once, recording visits
    for a, b in swaps:
        c1 = cow_at_pos[a]
        c2 = cow_at_pos[b]
        visited[c1].add(b)
        visited[c2].add(a)
        cow_at_pos[a], cow_at_pos[b] = c2, c1

    # Build permutation mapping each cow to its new position (as a cow ID)
    pos_of_cow = [0] * (N + 1)
    for pos in range(1, N + 1):
        c = cow_at_pos[pos]
        pos_of_cow[c] = pos

    ans = [0] * (N + 1)
    seen = [False] * (N + 1)

    # For each cycle in the permutation, union their visited positions
    for cow in range(1, N + 1):
        if not seen[cow]:
            cycle = []
            cur = cow
            while not seen[cur]:
                seen[cur] = True
                cycle.append(cur)
                cur = pos_of_cow[cur]
            # Union visited positions for the cycle
            union_set = set()
            for c in cycle:
                union_set |= visited[c]
            count = len(union_set)
            for c in cycle:
                ans[c] = count

    # Output results
    out = sys.stdout
    for cow in range(1, N + 1):
        out.write(str(ans[cow]) + '\n')


if __name__ == '__main__':
    main()
