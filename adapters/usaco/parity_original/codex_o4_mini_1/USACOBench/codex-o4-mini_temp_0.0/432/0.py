import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * (N+1)
    result = 0
    for i in range(1, N+1):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            count = [1, 0]
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        count[color[v]] += 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        print(-1)
                        return
            result += max(count)
    print(result)

if __name__ == "__main__":
    main()
