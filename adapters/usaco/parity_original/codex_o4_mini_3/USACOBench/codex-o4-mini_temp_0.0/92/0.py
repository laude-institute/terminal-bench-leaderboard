#!/usr/bin/env python3
import sys

def main():
    # Read input
    grid = [sys.stdin.readline().strip() for _ in range(9)]
    # Compute parity of initial bits for rows, columns, blocks
    brow = [sum(int(c) for c in row) & 1 for row in grid]
    bcol = [0]*9
    for j in range(9):
        bcol[j] = sum(int(grid[i][j]) for i in range(9)) & 1
    # Block parity per group (3 groups of 3 rows, 3 blocks per group)
    bblk = [0]*3
    for g in range(3):
        mask = 0
        for b in range(3):
            cnt = 0
            for i in range(3*g, 3*g+3):
                for j in range(3*b, 3*b+3):
                    cnt += int(grid[i][j])
            if cnt & 1:
                mask |= 1 << b
        bblk[g] = mask

    # Precompute block masks for columns
    block_masks = [0]*3
    for b in range(3):
        m = 0
        for j in range(3*b, 3*b+3):
            m |= 1 << j
        block_masks[b] = m

    # Precompute patterns by required row flip parity
    patterns = {0: [], 1: []}
    for p in range(1<<9):
        pc = p.bit_count() & 1
        # Compute block flip parity mask for this pattern
        blk = 0
        for b in range(3):
            if (p & block_masks[b]).bit_count() & 1:
                blk |= 1 << b
        patterns[pc].append((p, p.bit_count(), blk))

    # Target column mask
    target_col = 0
    for j in range(9):
        if bcol[j]:
            target_col |= 1 << j

    # DP over groups
    # dp: dict col_mask->min flips
    dp = {0: 0}
    for g in range(3):
        # Initialize group DP: (col_mask, blk_mask) -> cost
        group_dp = {(col_mask, 0): cost for col_mask, cost in dp.items()}
        # Process 3 rows in this group
        for r in range(3*g, 3*g+3):
            new_dp = {}
            need_par = brow[r]
            for (col_mask, blk_mask), cost in group_dp.items():
                for p, cnt, pblk in patterns[need_par]:
                    nc = col_mask ^ p
                    nb = blk_mask ^ pblk
                    nc_cost = cost + cnt
                    key = (nc, nb)
                    if key not in new_dp or nc_cost < new_dp[key]:
                        new_dp[key] = nc_cost
            group_dp = new_dp
        # End of group: enforce block parity
        dp = {}
        for (col_mask, blk_mask), cost in group_dp.items():
            if blk_mask == bblk[g]:
                if col_mask not in dp or cost < dp[col_mask]:
                    dp[col_mask] = cost
    # Final: enforce column parity
    res = dp.get(target_col, None)
    print(res if res is not None else -1)

if __name__ == '__main__':
    main()
