#!/usr/bin/env python3
"""
Fuel Economy

Minimize cost to travel from 0 to D with tank capacity G,
starting with B fuel, visiting N stations (Xi, Yi).
"""
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    G = int(next(it))
    B = int(next(it))
    D = int(next(it))
    stations = []
    for _ in range(N):
        x = int(next(it)); y = int(next(it))
        stations.append((x, y))
    # add destination as station with price 0
    stations.append((D, 0))
    stations.sort(key=lambda s: s[0])
    # initial feasibility
    if stations[0][0] > B:
        print(-1)
        return
    # compute next smaller price station index
    n = len(stations)
    nxt = [None] * n
    stack = []  # will store indices with increasing price
    for i in range(n - 1, -1, -1):
        _, price = stations[i]
        # pop until find smaller
        while stack and stations[stack[-1]][1] >= price:
            stack.pop()
        nxt[i] = stack[-1] if stack else None
        stack.append(i)
    # simulate
    fuel = B
    prev_x = 0
    cost = 0
    for i, (x, price) in enumerate(stations):
        dist = x - prev_x
        # check reachability
        if dist > G or fuel < dist:
            print(-1)
            return
        fuel -= dist
        prev_x = x
        # no need to buy at destination
        if x == D:
            break
        # determine desired fuel to leave station
        j = nxt[i]
        if j is not None and stations[j][0] - x <= G:
            desired = stations[j][0] - x
        else:
            desired = G
        if fuel < desired:
            buy = desired - fuel
            cost += buy * price
            fuel = desired
    print(cost)

if __name__ == '__main__':
    main()
