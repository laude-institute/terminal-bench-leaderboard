import sys
import heapq

def main():
    # Read input values
    N, A, B = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(N)]
    INF = 10**18
    max_time = 0
    # Possible movement directions
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Run Dijkstra from each starting pasture
    for si in range(N):
        for sj in range(N):
            # Initialize distances
            dist = [[INF] * N for _ in range(N)]
            dist[si][sj] = 0
            pq = [(0, si, sj)]
            while pq:
                d, i, j = heapq.heappop(pq)
                if d > dist[i][j]:
                    continue
                # Explore neighbors
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        # Determine move cost
                        w = A if grid[i][j] == grid[ni][nj] else B
                        nd = d + w
                        if nd < dist[ni][nj]:
                            dist[ni][nj] = nd
                            heapq.heappush(pq, (nd, ni, nj))
            # Update global maximum time
            for i in range(N):
                for j in range(N):
                    if dist[i][j] > max_time:
                        max_time = dist[i][j]

    # Output the result
    print(max_time)

if __name__ == '__main__':
    main()
