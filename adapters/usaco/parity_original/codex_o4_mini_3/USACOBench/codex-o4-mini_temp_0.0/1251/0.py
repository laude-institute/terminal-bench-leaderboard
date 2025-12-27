#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    costs = list(map(int, data[1:]))
    # Sort cow maximum tuitions
    costs.sort()
    best_revenue = 0
    best_tuition = 0
    # Evaluate revenue for each possible tuition
    for i, t in enumerate(costs):
        attendees = n - i
        revenue = t * attendees
        # Update if better revenue or tie with smaller tuition
        if revenue > best_revenue or (revenue == best_revenue and t < best_tuition):
            best_revenue = revenue
            best_tuition = t
    # Output the maximum revenue and optimal tuition
    print(best_revenue, best_tuition)

if __name__ == '__main__':
    main()
