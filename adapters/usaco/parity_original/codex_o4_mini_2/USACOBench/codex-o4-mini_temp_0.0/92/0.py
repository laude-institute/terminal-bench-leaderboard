#!/usr/bin/env python3
import sys

def main():
    # Read input grid
    grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
    # Parity requirements for rows, columns, and blocks
    p_row = [sum(grid[r]) & 1 for r in range(9)]
    p_col = [sum(grid[r][c] for r in range(9)) & 1 for c in range(9)]
    p_block = []
    for br in range(3):
        for bc in range(3):
            s = 0
            for r in range(br*3, br*3+3):
                for c in range(bc*3, bc*3+3):
                    s += grid[r][c]
            p_block.append(s & 1)

    # Precompute popcounts for 9-bit masks
    popcount = [bin(i).count('1') for i in range(1<<9)]
    # Masks by bit-parity
    masks_by_parity = {0: [], 1: []}
    for m in range(1<<9):
        masks_by_parity[popcount[m] & 1].append(m)

    # Precompute block masks for local blocks (3 per group)
    block_masks = []
    for k in range(3):
        mask = 0
        for j in range(9):
            if j // 3 == k:
                mask |= 1 << j
        block_masks.append(mask)

    # Compute cost_s for each of 3 groups of 3 rows
    cost_groups = []  # list of lists of length 512
    for g in range(3):
        # Rows and block parity for this group
        rows = range(g*3, g*3+3)
        row_par = [p_row[r] for r in rows]
        blk_par = [p_block[g*3 + k] for k in range(3)]
        # Local dp: key = (b<<9)|s, value = min cost
        dp = {}
        # First row
        for m in masks_by_parity[row_par[0]]:
            # block parity bits
            b = 0
            for k in range(3):
                if popcount[m & block_masks[k]] & 1:
                    b |= 1 << k
            s = m
            dp[(b << 9) | s] = popcount[m]
        # Next rows
        for ri in (1, 2):
            new_dp = {}
            for key, cost in dp.items():
                b_prev = key >> 9
                s_prev = key & 0x1FF
                for m in masks_by_parity[row_par[ri]]:
                    # update block parity and s
                    b_new = b_prev
                    for k in range(3):
                        if popcount[m & block_masks[k]] & 1:
                            b_new ^= 1 << k
                    s_new = s_prev ^ m
                    c = cost + popcount[m]
                    k2 = (b_new << 9) | s_new
                    # at last row, enforce block parity
                    if ri == 2:
                        # check block parity matches
                        ok = True
                        for k in range(3):
                            if ((b_new >> k) & 1) != blk_par[k]:
                                ok = False
                                break
                        if not ok:
                            continue
                    # record
                    prev = new_dp.get(k2)
                    if prev is None or c < prev:
                        new_dp[k2] = c
            dp = new_dp
        # Build cost_s
        cost_s = [float('inf')] * (1 << 9)
        for key, cost in dp.items():
            s = key & 0x1FF
            if cost < cost_s[s]:
                cost_s[s] = cost
        cost_groups.append(cost_s)

    # Combine groups by DP over column parity
    # dp_cols[c] = min cost to reach parity mask c
    INF = float('inf')
    dp_cols = [INF] * (1 << 9)
    dp_cols[0] = 0
    for cost_s in cost_groups:
        next_dp = [INF] * (1 << 9)
        for c_in, cost_in in enumerate(dp_cols):
            if cost_in == INF:
                continue
            # try all s with finite cost
            for s, c_s in enumerate(cost_s):
                if c_s == INF:
                    continue
                c_out = c_in ^ s
                nc = cost_in + c_s
                if nc < next_dp[c_out]:
                    next_dp[c_out] = nc
        dp_cols = next_dp

    # target column parity mask
    target = 0
    for j in range(9):
        if p_col[j]:
            target |= 1 << j
    # result
    print(dp_cols[target])

if __name__ == '__main__':
    main()
