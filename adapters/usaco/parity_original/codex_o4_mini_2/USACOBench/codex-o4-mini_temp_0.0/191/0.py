#!/usr/bin/env python3
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    A = int(data[1])
    B = int(data[2])
    grid = data[3:3+N]
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    INF = float('inf')
    answer = 0
    # Run Dijkstra from each cell
    for si in range(N):
        for sj in range(N):
            dist = [[INF]*N for _ in range(N)]
            dist[si][sj] = 0
            heap = [(0, si, sj)]
            while heap:
                d, x, y = heapq.heappop(heap)
                if d > dist[x][y]:
                    continue
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        cost = A if grid[x][y] == grid[nx][ny] else B
                        nd = d + cost
                        if nd < dist[nx][ny]:
                            dist[nx][ny] = nd
                            heapq.heappush(heap, (nd, nx, ny))
            # update maximum distance from this source
            local_max = max(dist[i][j] for i in range(N) for j in range(N))
            if local_max > answer:
                answer = local_max
    print(answer)

if __name__ == '__main__':
    main()
