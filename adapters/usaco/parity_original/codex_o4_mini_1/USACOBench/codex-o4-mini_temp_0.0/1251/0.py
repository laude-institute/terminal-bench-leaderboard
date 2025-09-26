#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    costs = list(map(int, data[1:]))
    # Sort the willingness values
    costs.sort()
    max_revenue = 0
    best_tuition = 0
    # Iterate over sorted costs, considering each as tuition
    for i, c in enumerate(costs):
        attendees = n - i
        revenue = c * attendees
        # Update max revenue or tie-break by smaller tuition
        if revenue > max_revenue or (revenue == max_revenue and c < best_tuition):
            max_revenue = revenue
            best_tuition = c
    # Output the result
    print(f"{max_revenue} {best_tuition}")

if __name__ == '__main__':
    main()
