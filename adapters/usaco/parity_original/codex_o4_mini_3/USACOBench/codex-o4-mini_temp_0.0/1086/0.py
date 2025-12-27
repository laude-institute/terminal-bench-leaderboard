#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    swaps = []
    idx = 2
    for _ in range(K):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        swaps.append((a, b))

    # cows[pos] = cow id at position pos
    cows = list(range(N+1))
    # visited positions for each cow id
    visited = [set([i]) for i in range(N+1)]

    # simulate one full round of swaps
    for a, b in swaps:
        cows[a], cows[b] = cows[b], cows[a]
        visited[cows[a]].add(a)
        visited[cows[b]].add(b)

    # build next mapping: after round, cow moves to position p, so nxt[cow] = p
    nxt = [0] * (N+1)
    for pos in range(1, N+1):
        cow = cows[pos]
        nxt[cow] = pos

    ans = [0] * (N+1)
    seen = [False] * (N+1)

    # decompose cycles and compute union of visited positions
    for cow in range(1, N+1):
        if not seen[cow]:
            cycle = []
            cur = cow
            while not seen[cur]:
                seen[cur] = True
                cycle.append(cur)
                cur = nxt[cur]
            # union all visited sets in cycle
            union_set = set()
            for c in cycle:
                union_set |= visited[c]
            cnt = len(union_set)
            for c in cycle:
                ans[c] = cnt

    # output results
    out = sys.stdout
    for i in range(1, N+1):
        out.write(str(ans[i]))
        out.write("\n")

if __name__ == '__main__':
    main()
