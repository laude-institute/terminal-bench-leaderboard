import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, l, c = map(int, input().split())
        edges.append((u-1, v-1, l, c))

    # Get unique capacities sorted descending
    caps = sorted({c for _, _, _, c in edges}, reverse=True)
    INF = 10**18
    best = INF

    # For each possible bottleneck capacity, find shortest path
    for cap in caps:
        # Build adjacency list using edges with capacity >= current cap
        adj = [[] for _ in range(N)]
        for u, v, l, c in edges:
            if c >= cap:
                adj[u].append((v, l))
                adj[v].append((u, l))

        # Dijkstra to find minimal latency from 0 to N-1
        dist = [INF] * N
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # If reachable, compute total time: latency + floor(X / cap)
        if dist[N-1] < INF:
            time = dist[N-1] + X // cap
            if time < best:
                best = time

    # Output the minimum time
    print(best)


if __name__ == "__main__":
    main()
