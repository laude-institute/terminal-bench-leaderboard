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
    # Build index map for active positions
    idx = {a: i for i, a in enumerate(A)}
    # Precompute next active for each index in A
    # Build static permutation M: after one minute, cow at x moves to M[x]
    Nmod = N
    M = [0] * Nmod
    for x in range(Nmod):
        j = idx.get(x, None)
        if j is not None:
            # active position: P0 maps x->A[(j+1)%K], then shift^{-1}
            nxt = A[(j+1) % K]
            M[x] = (nxt - 1) % Nmod
        else:
            # not active: stays, then shift^{-1}
            M[x] = (x - 1) % Nmod
    # Compute M^T via cycle decomposition
    T_mod = T  # for cycles, use T mod cycle length
    Mpow = [0] * Nmod
    vis = [False] * Nmod
    for i in range(Nmod):
        if not vis[i]:
            # build cycle starting at i
            cycle = []
            x = i
            while not vis[x]:
                vis[x] = True
                cycle.append(x)
                x = M[x]
            L = len(cycle)
            # steps to move in cycle
            step = T_mod % L
            # assign
            for idx_c, v in enumerate(cycle):
                Mpow[v] = cycle[(idx_c + step) % L]
    # Now apply final shift S^T: cow at initial pos j goes to pos = Mpow[j] + T mod N
    shift = T % Nmod
    # Build answer: ans[pos] = cow label j
    ans = [0] * Nmod
    for j in range(Nmod):
        pos = (Mpow[j] + shift) % Nmod
        ans[pos] = j
    # Output
    out = ' '.join(str(ans[i]) for i in range(Nmod))
    sys.stdout.write(out)

if __name__ == '__main__':
    main()
