# Problem Restatement:
# We have N cows each at a distinct coordinate x_i on a line, with some cows marked sick (1) and some healthy (0).
# A disease spreads transitively between any two cows within an unknown radius R: if any sick cow is within R units of another cow, that cow becomes sick, and so on.
# We observe the final pattern of sick cows and want to determine the minimum number of cows that must have been initially infected, over all R values consistent with the data.

# Conceptual Solution:
# 1. Any healthy cow must be more than R away from every sick cow, otherwise it would be sick. Thus R < min distance between any sick and healthy cow.
# 2. Let d = min|x_sick - x_healthy| over all sick and healthy pairs. Then the maximum possible R is R_max = d - 1 (integer coordinates).
# 3. Under this R_max, sick cows form clusters: sort sick cow positions, and split a new cluster whenever the gap between consecutive sick cows exceeds R_max.
# 4. The number of such clusters is the minimum number of initially infected cows.

# Pseudocode:
# read N
# read list of (x, s) pairs
# extract and sort sick_positions and healthy_positions
# if no healthy cows: print 1 and exit
# compute d = min distance between any sick and healthy (via binary search)
# R_max = d - 1
# sort sick_positions
# count = 1
# for i in 1..len(sick_positions)-1:
#     if sick_positions[i] - sick_positions[i-1] > R_max:
#         count += 1
# print count

import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    coords = list(map(int, data[1::2]))
    states = list(map(int, data[2::2]))
    sick = []
    healthy = []
    for x, s in zip(coords, states):
        if s == 1:
            sick.append(x)
        else:
            healthy.append(x)
    sick.sort()
    healthy.sort()
    # If there are no healthy cows, R can be arbitrarily large: one cluster
    if not healthy:
        print(1)
        return
    # Compute minimum distance between any sick and healthy cow
    dmin = None
    for x in sick:
        # find insertion point in healthy
        i = bisect.bisect_left(healthy, x)
        # check neighbor on left
        if i > 0:
            dist = x - healthy[i-1]
            dmin = dist if dmin is None or dist < dmin else dmin
        # check neighbor on right
        if i < len(healthy):
            dist = healthy[i] - x
            dmin = dist if dmin is None or dist < dmin else dmin
    # Maximum possible R is one less than this minimal distance
    R = dmin - 1
    # Count clusters among sick cows under gap > R
    clusters = 1
    for i in range(1, len(sick)):
        if sick[i] - sick[i-1] > R:
            clusters += 1
    print(clusters)

if __name__ == '__main__':
    main()
