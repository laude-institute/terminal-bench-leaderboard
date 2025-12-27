#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    A1, A2 = map(int, data[2:4])
    B1, B2 = map(int, data[4:6])

    # Build the permutation after one full iteration of two reversals
    # Start with identity positions
    positions = list(range(N+1))  # 1-indexed
    # First reversal A1..A2
    positions[A1:A2+1] = positions[A1:A2+1][::-1]
    # Second reversal B1..B2
    positions[B1:B2+1] = positions[B1:B2+1][::-1]

    # Invert positions to get mapping perm[i] = new position of element at i
    perm = [0] * (N+1)
    for new_pos in range(1, N+1):
        orig = positions[new_pos]
        perm[orig] = new_pos

    # Prepare answer and visited flags
    ans = [0] * (N+1)
    visited = [False] * (N+1)

    # Decompose into cycles and apply K steps
    for i in range(1, N+1):
        if not visited[i]:
            # Extract cycle starting at i
            cycle = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = perm[cur]
            L = len(cycle)
            step = K % L
            # Assign cows to their final positions
            for idx, orig in enumerate(cycle):
                dest = cycle[(idx + step) % L]
                ans[dest] = orig

    # Output final labels at each position
    out = []
    for pos in range(1, N+1):
        out.append(str(ans[pos]))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
