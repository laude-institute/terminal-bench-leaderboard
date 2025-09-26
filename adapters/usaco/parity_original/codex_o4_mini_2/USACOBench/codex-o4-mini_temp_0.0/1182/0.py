#!/usr/bin/env python3
"""
Solution to the soulmate personality transformation problem.
Operations allowed: multiply by 2, divide by 2 if even, add 1.
We perform a best-first search (Dijkstra) with an initial upper bound from a greedy heuristic.
"""
import sys
import heapq

def greedy_upper(x, y):
    """Compute a heuristic upper bound on operations from x to y."""
    u = x
    steps = 0
    # Greedy shrink until <= y
    while u > y:
        if u % 2 == 0:
            u //= 2
        else:
            u += 1
        steps += 1
    # Greedy grow until == y
    while u < y:
        if u * 2 <= y:
            u *= 2
        else:
            u += 1
        steps += 1
    return steps

def min_ops(x, y):
    """Compute minimum operations from x to y using Dijkstra with pruning."""
    if x == y:
        return 0
    # Bound state space
    limit = max(x, y) * 2 + 2
    # Initial upper bound
    best_ans = greedy_upper(x, y)
    # Priority queue: (cost, value)
    pq = [(0, x)]
    dist = {x: 0}
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u] or cost >= best_ans:
            continue
        if u == y:
            best_ans = cost
            continue
        # Division by 2
        if u % 2 == 0:
            v = u // 2
            nc = cost + 1
            if nc < dist.get(v, best_ans) and nc < best_ans:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
        # Multiplication by 2
        v = u * 2
        if v <= limit:
            nc = cost + 1
            if nc < dist.get(v, best_ans) and nc < best_ans:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
        # Addition by 1
        v = u + 1
        if v <= limit:
            nc = cost + 1
            if nc < dist.get(v, best_ans) and nc < best_ans:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
    return best_ans

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    idx = 1
    results = []
    for _ in range(n):
        x = int(data[idx]); y = int(data[idx+1])
        idx += 2
        results.append(str(min_ops(x, y)))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
