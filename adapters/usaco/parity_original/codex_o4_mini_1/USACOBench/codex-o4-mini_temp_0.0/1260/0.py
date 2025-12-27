#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    data = sys.stdin
    readline = data.readline
    INF = 10**30

    N, K = map(int, readline().split())
    w = [list(map(int, readline().split())) for _ in range(N)]
    Q = N * N
    rem = [tuple(map(lambda x: int(x)-1, readline().split())) for _ in range(Q)]

    # Prepare for reverse additions
    add = rem[::-1]

    # dist[k][v]: shortest dist from 0 to v using exactly k edges
    dist = [[INF] * N for _ in range(K+1)]
    dist[0][0] = 0

    # ans_rev_e[t]: answer after t additions (0..Q)
    ans_rev = [0] * (Q+1)
    # initial (0 edges)
    ans_rev[0] = -1

    target = N-1
    # process additions
    for t in range(1, Q+1):
        a, b = add[t-1]
        weight = w[a][b]
        # update dist for paths ending with this new edge
        for k in range(1, K+1):
            prev = dist[k-1][a]
            if prev + weight < dist[k][b]:
                dist[k][b] = prev + weight
        # record answer after t additions
        val = dist[K][target]
        ans_rev[t] = val if val < INF else -1

    # output answers after each removal
    out = sys.stdout.write
    for i in range(1, Q+1):
        # after i-th removal, graph has Q-i edges => ans_rev[Q-i]
        out(str(ans_rev[Q-i]) + '\n')

if __name__ == '__main__':
    main()
