#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    try:
        N = int(next(it))
    except StopIteration:
        return
    G = int(next(it))
    B = int(next(it))
    D = int(next(it))
    stations = []
    for _ in range(N):
        x = int(next(it)); y = int(next(it))
        stations.append((x, y))
    # Add destination as a station with price 0
    stations.append((D, 0))
    # Sort by distance
    stations.sort(key=lambda s: s[0])
    # Extract positions and prices
    X = [s[0] for s in stations]
    Y = [s[1] for s in stations]
    N = len(stations)
    # Compute next smaller-price station index
    next_sm = [-1] * N
    stack = []  # will store indices
    for i in range(N - 1, -1, -1):
        while stack and Y[stack[-1]] >= Y[i]:
            stack.pop()
        if stack:
            next_sm[i] = stack[-1]
        stack.append(i)

    # Initialize fuel and position
    fuel = min(B, G)
    pos = 0
    cost = 0
    # Traverse stations
    for i in range(N):
        dist = X[i] - pos
        # Check reachability
        if dist > G:
            print(-1)
            return
        fuel -= dist
        if fuel < 0:
            print(-1)
            return
        pos = X[i]
        # At destination
        if i == N - 1:
            break
        # Determine required fuel to next cheaper station or full tank
        j = next_sm[i]
        if j != -1 and X[j] - X[i] <= G:
            max_need = X[j] - X[i]
        else:
            max_need = G
        # Buy fuel if needed
        if fuel < max_need:
            buy = max_need - fuel
            cost += buy * Y[i]
            fuel += buy
    print(cost)

if __name__ == '__main__':
    main()
