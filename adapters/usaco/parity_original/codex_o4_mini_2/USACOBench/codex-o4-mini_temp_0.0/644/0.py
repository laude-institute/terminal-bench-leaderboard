#!/usr/bin/env python3
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    close_order = [int(input()) for _ in range(n)]

    closed = [False] * (n + 1)
    results = []

    # helper to check connectivity among open barns
    def is_connected(open_count):
        # find a start node
        start = -1
        for i in range(1, n+1):
            if not closed[i]:
                start = i
                break
        if start == -1:
            return True
        # bfs
        visited = [False] * (n + 1)
        dq = deque([start])
        visited[start] = True
        cnt = 1
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if not closed[v] and not visited[v]:
                    visited[v] = True
                    dq.append(v)
                    cnt += 1
        return cnt == open_count

    # initial state
    open_count = n
    results.append("YES" if is_connected(open_count) else "NO")

    # process closings
    for i in range(n):
        barn = close_order[i]
        closed[barn] = True
        open_count -= 1
        results.append("YES" if is_connected(open_count) else "NO")

    # output results: only first n lines (initial + after n-1 closings)
    # problem expects n lines: initial and after each of first n-1 closings
    # But sample shows n lines for n=4: initial + after 3 closings
    for i in range(n):
        print(results[i])

if __name__ == "__main__":
    main()
