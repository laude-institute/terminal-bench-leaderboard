#!/usr/bin/env python3
"""
Balanced Teams: Partition 12 cows into 4 teams of 3
to minimize the difference between the highest and lowest team sums.
"""
import sys
from itertools import combinations

def main():
    # Read 12 cow skill levels
    skills = [int(sys.stdin.readline()) for _ in range(12)]
    n = len(skills)
    indices = list(range(n))
    best_diff = float('inf')

    # Enumerate possible team assignments
    for team1 in combinations(indices, 3):
        rem1 = set(indices) - set(team1)
        for team2 in combinations(sorted(rem1), 3):
            rem2 = rem1 - set(team2)
            for team3 in combinations(sorted(rem2), 3):
                # team4 is the remaining cows
                team4 = tuple(sorted(rem2 - set(team3)))
                # enforce ordering by minimum index to avoid duplicates
                mins = [min(team1), min(team2), min(team3), min(team4)]
                if not (mins[0] < mins[1] < mins[2] < mins[3]):
                    continue

                # Compute team skill sums
                sums = [
                    sum(skills[i] for i in team)
                    for team in (team1, team2, team3, team4)
                ]
                diff = max(sums) - min(sums)
                if diff < best_diff:
                    best_diff = diff

    # Output the minimal possible difference
    print(best_diff)

if __name__ == '__main__':
    main()
