#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    # Build the inverse permutation after one full sequence of reversals
    perm = list(range(N))
    for _ in range(M):
        l = int(next(it)) - 1
        r = int(next(it)) - 1
        # reverse the segment [l, r]
        perm[l:r+1] = perm[l:r+1][::-1]
    # Prepare to compute K applications via cycle decomposition
    ans = [0] * N
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            cycle = []
            j = i
            # collect one cycle
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = perm[j]
            L = len(cycle)
            shift = K % L
            # assign final source for each position in the cycle
            for idx, node in enumerate(cycle):
                ans[node] = cycle[(idx + shift) % L]
    # Output labels (1-based)
    out = sys.stdout
    for i in range(N):
        out.write(str(ans[i] + 1))
        out.write("\n")

if __name__ == "__main__":
    main()
