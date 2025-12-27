#!/usr/bin/env python3
import sys
import heapq
import bisect

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    breeds = list(map(int, input().split()))
    # zero-index breeds
    breeds = [b-1 for b in breeds]
    S = [list(map(int, list(input().strip()))) for _ in range(K)]
    # positions by breed
    positions = [[] for _ in range(K)]
    for i, b in enumerate(breeds):
        positions[b].append(i)
    # distances and visited
    INF = 10**30
    dist = [INF] * N
    dist[0] = 0
    visited = [False] * N
    # use sorted lists for unvisited positions per breed
    unvisited = [list(lst) for lst in positions]
    pq = [(0, 0)]  # (dist, index)
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u == N-1:
            break
        b_u = breeds[u]
        # try transmissions to each breed
        for b_v in range(K):
            if S[b_u][b_v] == 0:
                continue
            lst = unvisited[b_v]
            # relax nearest candidates until no improvement
            while lst:
                idx = bisect.bisect_left(lst, u)
                cand = None
                # choose closer of successor and predecessor
                if idx < len(lst):
                    cand = lst[idx]
                    best_dist = abs(cand - u)
                if idx > 0:
                    prev = lst[idx-1]
                    d2 = abs(prev - u)
                    if cand is None or d2 < best_dist:
                        cand = prev
                        best_dist = d2
                # compute new distance
                newd = d + best_dist
                if newd < dist[cand]:
                    dist[cand] = newd
                    heapq.heappush(pq, (newd, cand))
                    # remove from unvisited for this breed
                    lst.pop(bisect.bisect_left(lst, cand))
                else:
                    break
    # output result
    res = dist[N-1]
    print(res if res < INF else -1)

if __name__ == '__main__':
    main()
