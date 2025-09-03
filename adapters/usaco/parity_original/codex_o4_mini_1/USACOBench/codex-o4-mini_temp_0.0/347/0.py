#!/usr/bin/env python3
"""
Problem: Count pairs of cows with unobstructed line of sight around a circular silo.

1. Restate:
   Given N points outside a circle of radius R centered at origin, count pairs whose connecting segment doesn't intersect the circle.

2. Concept:
   For each cow compute its polar angle φ and half-angle α of the circle as seen from it (α = arccos(R/d)).
   Two cows see each other iff both |φ_i - φ_j| <= α_i and <= α_j.
   Equivalently, for each cow i, count prior cows j where φ_i lies in [φ_j - α_j, φ_j + α_j] and φ_j lies in [φ_i - α_i, φ_i + α_i].
   We sweep angles by duplicating angles +2π to handle wrap, use events to add/remove active intervals for cows j, and query active j satisfying φ_j >= φ_i - α_i.

3. Pseudocode:
   Read N, R and points.
   For each cow i: compute d, φ in [0,2π), α = acos(R/d).
   For each i: create event at t_start = φ - α + 2π (add j), t_query = φ + 2π, t_end = φ + α + 2π (remove j).
   Collect all φ + 2π values, sort and compress for BIT index.
   Sort events by time; on add: BIT[pos_j]++, total++; on remove: BIT[pos_j]--, total--;
   on query: L = (φ_i+2π) - α_i; find first idx with key >= L; cnt = total - BIT.prefix(idx-1); record cnt.
   Answer = sum(cnt_i - 1) // 2; print.

4. Implementation below.
"""
import sys, math

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it)); R = float(next(it))
    cows = []
    for _ in range(N):
        x = float(next(it)); y = float(next(it))
        d = math.hypot(x, y)
        phi = math.atan2(y, x)
        if phi < 0: phi += 2*math.pi
        alpha = math.acos(R / d)
        cows.append((phi, alpha))

    # Prepare events and compression keys
    events = []  # (time, type, idx)
    keys = []
    for i, (phi, alpha) in enumerate(cows):
        t_add = phi - alpha + 2*math.pi
        t_q   = phi + 2*math.pi
        t_rem = phi + alpha + 2*math.pi
        events.append((t_add, 0, i))
        events.append((t_q,   1, i))
        events.append((t_rem, 2, i))
        keys.append(phi + 2*math.pi)

    # compress keys
    sorted_keys = sorted(keys)
    # BIT for counts
    M = len(sorted_keys)
    bit = [0] * (M + 1)
    def bit_add(i, v):
        i += 1
        while i <= M:
            bit[i] += v; i += i & -i
    def bit_sum(i):
        s = 0; i += 1
        while i > 0:
            s += bit[i]; i -= i & -i
        return s

    # map idx->position
    pos = [0]*N
    for i, k in enumerate(sorted_keys):
        # find original index of this key (may have duplicates?) but unique by construction
        pass
    # build reverse map from key to pos
    key_to_pos = {k: i for i, k in enumerate(sorted_keys)}
    for i, (phi, _) in enumerate(cows):
        key = phi + 2*math.pi
        pos[i] = key_to_pos[key]

    # sweep
    events.sort(key=lambda x: (x[0], x[1]))
    total = 0
    cnt = [0]*N
    for t, typ, i in events:
        if typ == 0:
            bit_add(pos[i], 1); total += 1
        elif typ == 2:
            bit_add(pos[i], -1); total -= 1
        else:
            phi, alpha = cows[i]
            q_time = phi + 2*math.pi
            L = q_time - alpha
            # find first key >= L
            lo = 0; hi = M
            while lo < hi:
                mid = (lo+hi)//2
                if sorted_keys[mid] < L: lo = mid+1
                else: hi = mid
            c = total - (bit_sum(lo-1) if lo > 0 else 0)
            cnt[i] = c

    # each cow counted itself; each pair counted twice
    ans = (sum(c - 1 for c in cnt) // 2)
    print(ans)

if __name__ == '__main__':
    main()
