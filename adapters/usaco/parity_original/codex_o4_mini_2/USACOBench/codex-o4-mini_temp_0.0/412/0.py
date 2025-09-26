#!/usr/bin/env python3
"""
Reads two permutations A and B of cows numbered 1..N and computes
the number of cyclic shifts needed to transform A into B, and the
length of the largest cycle (or -1 if none).
"""
def main():
    N = int(input().strip())
    A = [int(input().strip()) for _ in range(N)]
    B = [int(input().strip()) for _ in range(N)]
    # Map each cow number to its target position in B
    target_pos = {cow: idx for idx, cow in enumerate(B)}
    # Build permutation P: current index -> target index
    P = [target_pos[cow] for cow in A]
    visited = [False] * N
    cycle_count = 0
    max_cycle_len = 0
    for i in range(N):
        # Skip already visited or fixed points
        if visited[i] or P[i] == i:
            continue
        # Traverse the cycle starting at i
        length = 0
        cur = i
        while not visited[cur]:
            visited[cur] = True
            cur = P[cur]
            length += 1
        cycle_count += 1
        if length > max_cycle_len:
            max_cycle_len = length
    # If no cycles, set length to -1
    if cycle_count == 0:
        max_cycle_len = -1
    print(cycle_count, max_cycle_len)

if __name__ == '__main__':
    main()
