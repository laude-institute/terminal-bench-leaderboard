#!/usr/bin/env python3
import sys
def main():
    sys.setrecursionlimit(10**7)
    data = sys.stdin
    first = data.readline().split()
    if not first:
        return
    n, m = map(int, first)
    coords = [tuple(map(int, data.readline().split())) for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, data.readline().split())
        a -= 1; b -= 1
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * n
    ans = float('inf')
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            min_x = max_x = coords[i][0]
            min_y = max_y = coords[i][1]
            while stack:
                u = stack.pop()
                x, y = coords[u]
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
            if perimeter < ans:
                ans = perimeter
    print(ans)

if __name__ == '__main__':
    main()
