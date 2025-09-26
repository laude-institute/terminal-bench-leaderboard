import sys
import heapq

def dijkstra(n, adj, edges):
    """Compute shortest distances and track previous edges."""
    dist = [float('inf')] * n
    prev_edge = [-1] * n
    dist[0] = 0
    heap = [(0, 0)]  # (distance, node)
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, ei in adj[u]:
            w = edges[ei][2]
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev_edge[v] = ei
                heapq.heappush(heap, (nd, v))
    return dist, prev_edge

def main():
    data = sys.stdin.read().split()
    n, m = map(int, data[:2])
    edges = []  # each edge: [u, v, weight]
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        a = int(data[idx]) - 1
        b = int(data[idx+1]) - 1
        l = int(data[idx+2])
        idx += 3
        edges.append([a, b, l])
        ei = len(edges) - 1
        adj[a].append((b, ei))
        adj[b].append((a, ei))

    # Initial shortest path
    dist, prev_edge = dijkstra(n, adj, edges)
    orig = dist[n-1]

    # Reconstruct the edges on one shortest path
    path_edges = []
    node = n - 1
    while node != 0:
        ei = prev_edge[node]
        path_edges.append(ei)
        u, v, _ = edges[ei]
        node = u if v == node else v

    # Try doubling each edge on the path
    max_diff = 0
    for ei in path_edges:
        # Double weight
        edges[ei][2] *= 2
        dist2, _ = dijkstra(n, adj, edges)
        new_dist = dist2[n-1]
        max_diff = max(max_diff, new_dist - orig)
        # Restore weight
        edges[ei][2] //= 2

    print(max_diff)

if __name__ == "__main__":
    main()
