#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    N = int(data.readline())
    a = [0] * (N + 1)
    v = [0] * (N + 1)
    total = 0
    for i in range(1, N+1):
        ai, vi = map(int, data.readline().split())
        a[i] = ai
        v[i] = vi
        total += vi

    visited = [0] * (N + 1)  # 0=unvisited,1=visiting,2=done
    pos = [-1] * (N + 1)
    sum_mins = 0

    for i in range(1, N+1):
        if visited[i] != 0:
            continue
        stack = []
        u = i
        # traverse until hit visited node
        while visited[u] == 0:
            pos[u] = len(stack)
            stack.append(u)
            visited[u] = 1
            u = a[u]
        # if found a cycle, process it
        if visited[u] == 1:
            # cycle nodes are stack[pos[u]:]
            idx = pos[u]
            # find minimum v in the cycle
            min_v = min(v[node] for node in stack[idx:])
            sum_mins += min_v
        # mark all in stack as done
        for node in stack:
            visited[node] = 2
            pos[node] = -1

    # result is total v minus sum of minima of each cycle
    result = total - sum_mins
    print(result)

if __name__ == '__main__':
    main()
