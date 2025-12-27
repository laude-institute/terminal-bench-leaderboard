#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    cows = []  # list of (dir, x, y, idx)
    for i in range(N):
        d, x, y = input().split()
        cows.append((d, int(x), int(y), i))
    # Separate east and north cows
    east = [(x, y, i) for d, x, y, i in cows if d == 'E']
    north = [(x, y, i) for d, x, y, i in cows if d == 'N']
    # Sort east by y ascending, north by x ascending
    east.sort(key=lambda e: e[1])  # y
    north.sort(key=lambda n: n[0])  # x
    # Initialize stop times and stoppers
    INF = float('inf')
    stop_time = [INF] * N
    stopper = [-1] * N
    # Determine stopping events
    for xe, ye, ie in east:
        for xn, yn, in_idx in north:
            # Check if paths cross
            if xe < xn and yn < ye:
                # Times to reach intersection
                te = xn - xe
                tn = ye - yn
                # If both still moving at that time
                if te < tn:
                    # east arrives first, north may stop
                    if te < stop_time[ie] and tn < stop_time[in_idx]:
                        stop_time[in_idx] = tn
                        stopper[in_idx] = ie
                elif tn < te:
                    # north arrives first, east may stop
                    if tn < stop_time[in_idx] and te < stop_time[ie]:
                        stop_time[ie] = te
                        stopper[ie] = in_idx
                # if equal, they pass through
    # Build blame graph
    children = [[] for _ in range(N)]
    for i, p in enumerate(stopper):
        if p != -1:
            children[p].append(i)
    # Count descendants with DFS
    sys.setrecursionlimit(10000)
    def dfs(u):
        cnt = 0
        for v in children[u]:
            cnt += 1 + dfs(v)
        return cnt
    # Output blame counts
    for i in range(N):
        print(dfs(i))

if __name__ == '__main__':
    main()
