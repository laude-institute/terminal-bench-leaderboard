#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # f[i] is the cow to which i forwards (0 means none)
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = int(data[i])
    # state: 0=unknown, 1=non-loopy, 2=loopy
    state = [0] * (n + 1)
    for i in range(1, n + 1):
        if state[i] != 0:
            continue
        u = i
        path = []
        visited = {}
        status = False
        # Follow pointers until sink, known state, or cycle
        while True:
            if u == 0:
                status = True
                break
            if state[u] == 1:
                status = True
                break
            if state[u] == 2:
                status = False
                break
            if u in visited:
                status = False
                break
            visited[u] = len(path)
            path.append(u)
            u = f[u]
        # Mark all on path accordingly
        for node in path:
            state[node] = 1 if status else 2
    # Count non-loopy cows
    result = sum(1 for i in range(1, n + 1) if state[i] == 1)
    print(result)

if __name__ == "__main__":
    main()
