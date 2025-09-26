#!/usr/bin/env python3
"""
Solution for Farmer John's cow university tuition problem.
Reads N and list of maximum tuition each cow will pay.
Determines the tuition that maximizes total revenue (tuition * attendees).
Prints the maximum revenue and smallest tuition achieving it.
"""

import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    costs = list(map(int, data[1:]))
    costs.sort()
    max_revenue = 0
    best_tuition = 0
    for i, t in enumerate(costs):
        attendees = n - i
        revenue = t * attendees
        if revenue > max_revenue:
            max_revenue = revenue
            best_tuition = t
    print(max_revenue, best_tuition)

if __name__ == '__main__':
    main()
