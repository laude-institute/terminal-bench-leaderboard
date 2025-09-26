#!/usr/bin/env python3
"""
Reordering the Cows: Count number of cycles and max cycle length
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read initial and target orderings
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(n)]
    # Build mapping f: cow_id -> cow_id
    f = [0] * (n + 1)
    for a, b in zip(A, B):
        f[a] = b

    visited = [False] * (n + 1)
    num_cycles = 0
    max_len = 0

    # Traverse each cow to find cycles
    for cow in range(1, n + 1):
        if not visited[cow] and f[cow] != cow:
            # Start a new cycle
            curr = cow
            length = 0
            while not visited[curr]:
                visited[curr] = True
                curr = f[curr]
                length += 1
            num_cycles += 1
            if length > max_len:
                max_len = length

    # If no cycles, max length is -1
    if num_cycles == 0:
        max_len = -1

    # Output result
    print(f"{num_cycles} {max_len}")

if __name__ == '__main__':
    main()
