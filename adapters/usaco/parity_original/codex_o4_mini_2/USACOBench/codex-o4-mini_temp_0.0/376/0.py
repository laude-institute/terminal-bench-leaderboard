#!/usr/bin/env python3
# Ski Course Design solution for USACO

def main():
    import sys
    input = sys.stdin.readline

    # Read input
    N = int(input())
    hills = [int(input()) for _ in range(N)]

    # Initialize minimum cost to a large value
    min_cost = float('inf')

    # Try every possible low endpoint of the allowed height interval
    for low in range(0, 101 - 17):
        high = low + 17
        cost = 0
        # Calculate adjustment cost for each hill
        for h in hills:
            if h < low:
                d = low - h
                cost += d * d
            elif h > high:
                d = h - high
                cost += d * d
        # Update minimum cost
        if cost < min_cost:
            min_cost = cost

    # Output the result
    print(min_cost)

if __name__ == '__main__':
    main()
