"""
Solution to the COWVID-19 spread problem.
Compute minimum days to infect all farms in a tree.

Approach:
1. Compute sum of depths of all nodes from root (farm 1). Each depth step costs one movement day.
2. Compute minimum doublings needed so total infected cows >= N.
3. Total days = (sum of depths) + (number of doublings).
"""
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # build adjacency list
    adj = [[] for _ in range(n+1)]
    idx = 1
    for _ in range(n-1):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        adj[a].append(b)
        adj[b].append(a)
    # BFS to compute depths sum
    from collections import deque
    depth = [-1] * (n+1)
    q = deque([1])
    depth[1] = 0
    sum_depths = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                sum_depths += depth[v]
                q.append(v)
    # compute doublings
    doublings = 0
    cows = 1
    while cows < n:
        cows <<= 1
        doublings += 1
    # answer is movement days + doubling days
    print(doublings + sum_depths)

if __name__ == '__main__':
    main()
