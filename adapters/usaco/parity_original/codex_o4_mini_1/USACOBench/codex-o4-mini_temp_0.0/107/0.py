#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    bales = list(map(int, data[1:]))
    # Sort in descending order for better pruning
    bales.sort(reverse=True)
    total = sum(bales)
    # Initialize best answer as total (worst case all in one barn)
    best = [total]
    # Current sums of the three barns
    sums = [0, 0, 0]

    def dfs(i):
        # Use best[0] for mutable capture
        if i == n:
            current_max = max(sums)
            if current_max < best[0]:
                best[0] = current_max
            return
        # Prune branches that cannot improve
        if max(sums) >= best[0]:
            return
        seen = set()
        # Try placing bale i in each barn
        for j in range(3):
            # Avoid symmetric states: skip if this sum seen before
            if sums[j] in seen:
                continue
            seen.add(sums[j])
            # Only place in the first empty barn to avoid permutations
            if sums[j] == 0 and j > 0:
                break
            # Place bale i
            sums[j] += bales[i]
            dfs(i + 1)
            sums[j] -= bales[i]

    dfs(0)
    # Output the minimal largest share
    print(best[0])

if __name__ == '__main__':
    main()
