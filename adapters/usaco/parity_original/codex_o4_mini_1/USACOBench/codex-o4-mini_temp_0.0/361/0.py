"""
Solution to Milk Scheduling problem (msched).
1. Restatement:
   Given N cows, each takes 1 unit time to milk and yields g_i gallons if milked by deadline d_i.
   Schedule milkings to maximize total gallons without missing deadlines.
2. Concept:
   Use a greedy algorithm: sort cows by descending gallons. For each cow, schedule it at the latest
   available time slot on or before its deadline. Use a union-find (disjoint set) to track free slots.
3. Pseudocode:
   Read N and list of (g, d).
   Sort cows by g descending.
   Initialize parent array for union-find of size max_deadline+1.
   Define find(x): path-compression to find available slot <= x.
   For each cow:
       slot = find(d)
       if slot > 0:
           total += g
           union(slot, slot-1)
   Print total.
4. Implementation below.
"""

import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cows = []
    idx = 1
    max_d = 0
    for _ in range(n):
        g = int(data[idx]); d = int(data[idx+1])
        idx += 2
        cows.append((g, d))
        if d > max_d:
            max_d = d

    # Sort by descending gallons
    cows.sort(key=lambda x: x[0], reverse=True)

    # Union-find parent array
    parent = list(range(max_d + 1))

    def find(x):
        # find root with path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # link x's root to y's root
        rx = find(x)
        ry = find(y)
        parent[rx] = ry

    total = 0
    for g, d in cows:
        available = find(d)
        if available > 0:
            total += g
            union(available, available - 1)

    print(total)

if __name__ == "__main__":
    main()
