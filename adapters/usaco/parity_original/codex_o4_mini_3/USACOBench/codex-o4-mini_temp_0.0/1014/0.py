#!/usr/bin/env python3
"""
Solution to the cow line reversal problem.
Computes the permutation of positions induced by one full sequence of reversals,
then applies it K times via cycle decomposition.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    # Read reversal intervals, convert to 0-based indices
    reversals = []
    for _ in range(m):
        l = int(next(it)) - 1
        r = int(next(it)) - 1
        reversals.append((l, r))

    # Build permutation P: P[i] = position where element at i moves after one sequence
    P = [0] * n
    for i in range(n):
        pos = i
        for l, r in reversals:
            if l <= pos <= r:
                pos = l + r - pos
        P[i] = pos

    # Prepare result array and visited marker for cycle decomposition
    result = [0] * n
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # Gather one cycle
            cycle = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = P[cur]
            length = len(cycle)
            # Compute shift within cycle
            shift = k % length
            # Place each element's label into its final position
            for idx, src in enumerate(cycle):
                dst = cycle[(idx + shift) % length]
                result[dst] = src + 1

    # Output final ordering, one per line
    out = '\n'.join(str(x) for x in result)
    sys.stdout.write(out)

if __name__ == '__main__':
    main()
