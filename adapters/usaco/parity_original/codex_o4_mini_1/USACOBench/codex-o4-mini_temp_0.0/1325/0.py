#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    T = int(next(it))
    A = [int(next(it)) for _ in range(K)]
    # Build static permutation Q in rotating frame
    Q = list(range(N))
    # Default: Q[z] = (z+1) mod N
    for z in range(N):
        Q[z] = (z + 1) % N
    # Override special positions: if z = (A[i+1]-1 mod N), Q[z] = A[i]
    for i in range(K):
        prev_d = A[i]
        next_d = A[(i + 1) % K]
        z = (next_d - 1) % N
        Q[z] = prev_d

    # Compute Q^T via cycle decomposition
    visited = [False] * N
    cprime = [0] * N
    for z in range(N):
        if not visited[z]:
            # extract cycle
            cycle = []
            cur = z
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = Q[cur]
            L = len(cycle)
            shift = T % L
            # assign final positions in cycle
            for idx, node in enumerate(cycle):
                cprime[node] = cycle[(idx + shift) % L]

    # Map back to absolute frame
    offset = T % N
    out = [0] * N
    for x in range(N):
        y = (x - offset) % N
        out[x] = cprime[y]

    # Print result
    print(" ".join(str(c) for c in out))


if __name__ == '__main__':
    main()
