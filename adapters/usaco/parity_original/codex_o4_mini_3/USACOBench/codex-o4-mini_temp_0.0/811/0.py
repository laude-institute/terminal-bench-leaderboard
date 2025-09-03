#!/usr/bin/env python3
import sys
import heapq

def main():
    input = sys.stdin.readline
    N, B = map(int, input().split())
    f = [0] + list(map(int, input().split()))  # snow depths, 1-indexed
    s = [0] * (B+1)
    d = [0] * (B+1)
    for i in range(1, B+1):
        s[i], d[i] = map(int, input().split())

    INF = 10**18
    # dist[i][k]: min discards to reach tile i wearing boot k (0 = no boots)
    dist = [[INF] * (B+1) for _ in range(N+1)]
    dist[1][0] = 0
    # priority queue: (discards, tile, boot_index)
    pq = [(0, 1, 0)]

    while pq:
        disc, i, k = heapq.heappop(pq)
        if disc != dist[i][k]:
            continue
        # reached barn
        if i == N:
            print(disc)
            return

        # if not wearing boots, must put on a pair
        if k == 0:
            # can only put on topmost by discarding earlier ones
            # try each j as first worn boot
            for j in range(1, B+1):
                if s[j] >= f[i]:  # can stand here
                    cost = disc + (j - 1)
                    if cost < dist[i][j]:
                        dist[i][j] = cost
                        heapq.heappush(pq, (cost, i, j))
        else:
            # step forward up to d[k]
            max_step = min(N, i + d[k])
            for j in range(i+1, max_step+1):
                if f[j] <= s[k] and disc < dist[j][k]:
                    dist[j][k] = disc
                    heapq.heappush(pq, (disc, j, k))
            # change boots at current tile
            for j in range(k+1, B+1):
                if s[j] >= f[i]:
                    # discard boots between k+1..j-1 and old boot k
                    cost = disc + (j - k - 1) + 1
                    if cost < dist[i][j]:
                        dist[i][j] = cost
                        heapq.heappush(pq, (cost, i, j))

if __name__ == '__main__':
    main()
