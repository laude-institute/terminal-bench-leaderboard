#!/usr/bin/env python3
"""
Solution for Distant Pastures.
Reads N, A, B and the grid, computes the maximum shortest-path time
between any two pastures using Dijkstra's algorithm from each cell.
"""
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N, A, B = map(int, data[:3])
    lines = data[3:]
    grid = [list(line) for line in lines]
    INF = 10**30
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_time = 0
    # Run Dijkstra from each cell
    for si in range(N):
        for sj in range(N):
            dist = [[INF] * N for _ in range(N)]
            dist[si][sj] = 0
            heap = [(0, si, sj)]
            while heap:
                d, x, y = heapq.heappop(heap)
                if d > dist[x][y]:
                    continue
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        w = A if grid[x][y] == grid[nx][ny] else B
                        nd = d + w
                        if nd < dist[nx][ny]:
                            dist[nx][ny] = nd
                            heapq.heappush(heap, (nd, nx, ny))
            # update global maximum
            for row in dist:
                local_max = max(row)
                if local_max > max_time:
                    max_time = local_max
    print(max_time)

if __name__ == '__main__':
    main()
