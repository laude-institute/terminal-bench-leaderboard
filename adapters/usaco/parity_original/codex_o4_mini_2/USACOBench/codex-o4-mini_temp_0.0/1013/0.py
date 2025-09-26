#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    A1 = int(next(it)) - 1
    A2 = int(next(it)) - 1
    B1 = int(next(it)) - 1
    B2 = int(next(it)) - 1
    # Initialize cows labels 0..N-1
    a = list(range(N))
    # First reversal
    a[A1:A2+1] = reversed(a[A1:A2+1])
    # Second reversal
    a[B1:B2+1] = reversed(a[B1:B2+1])
    # Build permutation f: f[j] = new position of cow from old position j
    f = [0] * N
    for new_pos, old_label in enumerate(a):
        f[old_label] = new_pos
    # Compute f^K via cycle decomposition
    fk = [0] * N
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            # build cycle
            cycle = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = f[cur]
            L = len(cycle)
            # assign mappings
            shift = K % L
            for idx, val in enumerate(cycle):
                fk[val] = cycle[(idx + shift) % L]
    # Build final arrangement: ans[pos] = label
    ans = [0] * N
    for label in range(N):
        pos = fk[label]
        ans[pos] = label
    # Output labels as 1-indexed
    out = sys.stdout
    for label in ans:
        out.write(str(label+1))
        out.write("\n")

if __name__ == '__main__':
    main()
