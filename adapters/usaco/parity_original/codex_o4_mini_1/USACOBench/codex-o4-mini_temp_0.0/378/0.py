import sys
import itertools

def main():
    # Read skill levels for 12 cows
    skills = [int(sys.stdin.readline()) for _ in range(12)]
    best_diff = float('inf')
    indices = list(range(12))
    # Try all ways to form four teams of 3 by combinations
    for team1 in itertools.combinations(indices, 3):
        sum1 = sum(skills[i] for i in team1)
        rem1 = [i for i in indices if i not in team1]
        for team2 in itertools.combinations(rem1, 3):
            sum2 = sum(skills[i] for i in team2)
            rem2 = [i for i in rem1 if i not in team2]
            for team3 in itertools.combinations(rem2, 3):
                sum3 = sum(skills[i] for i in team3)
                team4 = [i for i in rem2 if i not in team3]
                sum4 = sum(skills[i] for i in team4)
                # Compute current max-min difference
                mx = max(sum1, sum2, sum3, sum4)
                mn = min(sum1, sum2, sum3, sum4)
                diff = mx - mn
                if diff < best_diff:
                    best_diff = diff
    # Output result
    print(best_diff)

if __name__ == '__main__':
    main()
