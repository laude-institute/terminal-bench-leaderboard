#!/usr/bin/env python3
"""
Solution to Fair Photography problem.
"""
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    cows = [tuple(map(int, input().split())) for _ in range(N)]
    # Sort cows by position
    cows.sort(key=lambda x: x[0])
    ans = -1
    # Enumerate subsets of breeds (1..8) with at least K breeds
    for mask in range(1 << 8):
        if bin(mask).count("1") < K:
            continue
        # Build list of breeds in this subset and a mapping to indices
        S = [b + 1 for b in range(8) if mask & (1 << b)]
        M = len(S)
        breed_to_idx = {S[i]: i for i in range(M)}
        # Initial vector = zeros for differences of counts
        zero_vec = tuple([0] * (M - 1))
        # mapping from diff vector -> earliest prefix index
        mapping = {zero_vec: 0}
        counts = [0] * M
        # positions within current valid segment (1-indexed)
        seg_positions = [None]
        seg_index = 0
        # Sweep through cows, splitting on forbidden breeds
        for x, b in cows:
            if b not in breed_to_idx:
                # Reset segment
                mapping.clear()
                mapping[zero_vec] = 0
                counts = [0] * M
                seg_positions = [None]
                seg_index = 0
                continue
            # Update counts and positions
            idx = breed_to_idx[b]
            counts[idx] += 1
            seg_index += 1
            seg_positions.append(x)
            # Build diff vector relative to counts[0]
            base = counts[0]
            diff = tuple(counts[i] - base for i in range(1, M))
            # Check for previous occurrence
            if diff in mapping:
                p = mapping[diff]
                # Interval cows p+1..seg_index inclusive
                left_pos = seg_positions[p + 1]
                size = x - left_pos
                if size > ans:
                    ans = size
            else:
                mapping[diff] = seg_index
    # Output result
    print(ans)

if __name__ == '__main__':
    main()
