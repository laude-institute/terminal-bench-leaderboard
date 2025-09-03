#!/usr/bin/env python3
"""
Minimum fuel cost to reach destination with greedy strategy.
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    G = int(next(it))
    B = int(next(it))
    D = int(next(it))
    stations = []
    for _ in range(N):
        x = int(next(it)); y = int(next(it))
        stations.append((x, y))
    # Add destination as station with zero price
    stations.append((D, 0))
    # Sort by distance
    stations.sort(key=lambda t: t[0])
    N = len(stations)
    # Compute next cheaper station index using monotonic stack
    next_cheaper = [-1] * N
    stack = []  # will store indices
    for i, (_, price) in enumerate(stations):
        while stack and price < stations[stack[-1]][1]:
            j = stack.pop()
            next_cheaper[j] = i
        stack.append(i)
    # Simulate travel and refueling
    curr_fuel = B
    prev_x = 0
    cost = 0
    for i, (x, price) in enumerate(stations):
        dist = x - prev_x
        # Can't reach this station
        if curr_fuel < dist:
            print(-1)
            return
        curr_fuel -= dist
        # If at destination, done
        if x == D:
            break
        # Determine target fuel to leave this station
        j = next_cheaper[i]
        if j != -1 and stations[j][0] - x <= G:
            target = stations[j][0] - x
        else:
            # Fill enough to either reach end or fill capacity
            target = min(G, D - x)
        # Buy fuel if needed
        if curr_fuel < target:
            buy = target - curr_fuel
            cost += buy * price
            curr_fuel += buy
        prev_x = x
    # Output total cost
    print(cost)

if __name__ == '__main__':
    main()
