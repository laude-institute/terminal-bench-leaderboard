#!/usr/bin/env python3
"""
Solution for Message Relay problem.
"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # F[i] = cow to which cow i forwards messages (0 if none)
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(input())

    # status: 0=unknown, 1=visiting, 2=non-loopy, 3=loopy
    status = [0] * (N + 1)

    for i in range(1, N + 1):
        if status[i] != 0:
            continue
        path = []
        cur = i
        while True:
            if status[cur] == 0:
                status[cur] = 1
                path.append(cur)
                nxt = F[cur]
                if nxt == 0:
                    # reached end, all on path are non-loopy
                    for node in path:
                        status[node] = 2
                    break
                cur = nxt
            else:
                if status[cur] == 1:
                    # found a cycle, all path cows are loopy
                    for node in path:
                        status[node] = 3
                else:
                    # leads to known status (non-loopy or loopy)
                    for node in path:
                        status[node] = status[cur]
                break

    # count non-loopy cows
    result = sum(1 for i in range(1, N + 1) if status[i] == 2)
    print(result)

if __name__ == "__main__":
    main()
