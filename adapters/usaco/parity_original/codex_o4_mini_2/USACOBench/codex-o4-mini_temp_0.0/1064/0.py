#!/usr/bin/env python3
import sys

def main():
    import sys
    input = sys.stdin.readline
    INF = 10**18
    N = int(input().strip())
    dir = []
    x = []
    y = []
    for _ in range(N):
        d, xi, yi = input().split()
        dir.append(d)
        x.append(int(xi))
        y.append(int(yi))
    # Prepare events: (loser_time, stopper_time, loser, stopper)
    events = []
    for i in range(N):
        if dir[i] != 'E':
            continue
        for j in range(N):
            if dir[j] != 'N':
                continue
            dx = x[j] - x[i]
            dy = y[i] - y[j]
            if dx < 0 or dy < 0:
                continue
            if dx < dy:
                # East arrives first, stops North at dy
                events.append((dy, dx, j, i))
            elif dy < dx:
                # North arrives first, stops East at dx
                events.append((dx, dy, i, j))
            # if equal, they pass
    # Process events by increasing loser arrival time
    events.sort(key=lambda e: e[0])
    stop_time = [INF] * N
    adj = [[] for _ in range(N)]
    for t_loser, t_stopper, loser, stopper in events:
        if stop_time[loser] == INF and stop_time[stopper] > t_stopper:
            stop_time[loser] = t_loser
            adj[stopper].append(loser)

    # Compute blame via subtree sizes
    sys.setrecursionlimit(10000)
    def count_sub(u):
        total = 0
        for v in adj[u]:
            total += 1 + count_sub(v)
        return total

    for i in range(N):
        print(count_sub(i))

if __name__ == '__main__':
    main()
