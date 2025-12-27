#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    dirs = []
    xs = []
    ys = []
    idx = 1
    for i in range(n):
        d = data[idx]; x = int(data[idx+1]); y = int(data[idx+2])
        dirs.append(d)
        xs.append(x)
        ys.append(y)
        idx += 3
    # Events: (stop_time, stopper, stopped, stopper_arrival_time)
    INF = 10**30
    events = []
    for i in range(n):
        for j in range(n):
            if dirs[i] == 'E' and dirs[j] == 'N':
                x_e, y_e = xs[i], ys[i]
                x_n, y_n = xs[j], ys[j]
                if x_e < x_n and y_n < y_e:
                    t_e = x_n - x_e
                    t_n = y_e - y_n
                    if t_e < t_n:
                        events.append((t_n, i, j, t_e))
                    elif t_n < t_e:
                        events.append((t_e, j, i, t_n))
            # other order will be covered when swapped
    # Sort by stop_time
    events.sort(key=lambda x: x[0])
    stop_time = [INF] * n
    children = [[] for _ in range(n)]
    # Process events
    for t_stop, stopper, stopped, t_stopper in events:
        if stop_time[stopped] == INF and stop_time[stopper] > t_stopper:
            stop_time[stopped] = t_stop
            children[stopper].append(stopped)
    # Compute blame via DFS
    blame = [0] * n
    for i in range(n):
        # DFS from i
        stack = children[i][:]
        cnt = 0
        while stack:
            u = stack.pop()
            cnt += 1
            for v in children[u]:
                stack.append(v)
        blame[i] = cnt
    # Output
    out = []
    for v in blame:
        out.append(str(v))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
