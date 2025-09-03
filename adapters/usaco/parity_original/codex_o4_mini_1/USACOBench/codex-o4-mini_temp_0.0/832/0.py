#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    # Read social hierarchy sequence
    seq = [int(next(it)) for _ in range(M)]
    # Read fixed position constraints
    fixed_pos = {}    # position -> cow
    cow_fixed = {}    # cow -> position
    for _ in range(K):
        c = int(next(it)); p = int(next(it))
        fixed_pos[p] = c
        cow_fixed[c] = p
    # If cow 1 already has a fixed position, that's the answer
    if 1 in cow_fixed:
        print(cow_fixed[1])
        return

    def feasible(cow_to_pos):
        """
        Check if there is a valid ordering given cow_to_pos fixed mappings.
        cow_to_pos: dict mapping cow -> fixed position
        """
        # Build position -> cow map from cow_to_pos
        pos_to_cow = {pos: cow for cow, pos in cow_to_pos.items()}
        # Build graph and in-degrees from hierarchy sequence
        in_deg = [0] * (N + 1)
        adj = [[] for _ in range(N + 1)]
        for i in range(len(seq) - 1):
            u = seq[i]; v = seq[i+1]
            adj[u].append(v)
            in_deg[v] += 1
        # Track placed cows
        placed = [False] * (N + 1)
        # Mutable copy of in-degrees
        deg = in_deg[:]
        # Simulate filling positions 1..N
        for pos in range(1, N + 1):
            if pos in pos_to_cow:
                cow = pos_to_cow[pos]
                # Cow must be available (in-degree zero and not yet placed)
                if placed[cow] or deg[cow] != 0:
                    return False
            else:
                # Pick any available cow with deg zero
                cow = -1
                for c in range(1, N + 1):
                    if not placed[c] and deg[c] == 0:
                        cow = c
                        break
                if cow == -1:
                    return False
            # Place the cow and update neighbors
            placed[cow] = True
            for nb in adj[cow]:
                deg[nb] -= 1
        return True

    # Try earliest possible position for cow 1
    for pos in range(1, N + 1):
        if pos in fixed_pos:
            continue
        # Assign cow 1 to this position
        assign = cow_fixed.copy()
        assign[1] = pos
        if feasible(assign):
            print(pos)
            return

if __name__ == '__main__':
    main()
