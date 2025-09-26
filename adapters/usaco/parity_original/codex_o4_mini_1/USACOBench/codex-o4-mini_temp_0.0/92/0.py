#!/usr/bin/env python3
"""
Solve Binary Sudoku: minimal bit toggles so every row, column,
and 3x3 subgrid has even parity.
"""
import sys

def read_board():
    grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
    return grid

def popcount(x):
    return x.bit_count()

def main():
    grid = read_board()
    # initial parities
    row_par = [sum(grid[i][j] for j in range(9)) & 1 for i in range(9)]
    col_par = [sum(grid[i][j] for i in range(9)) & 1 for j in range(9)]
    block_par = []  # 3 bands of 3 blocks
    for bi in range(3):
        for bj in range(3):
            s = 0
            for di in range(3):
                for dj in range(3):
                    s += grid[3*bi+di][3*bj+dj]
            block_par.append(s & 1)
    # Precompute per-block valid flips
    # block_masks[band][block] = {r_mask: [(c_global_mask, weight), ...], ...}
    block_masks = [[{} for _ in range(3)] for _ in range(3)]
    for bi in range(3):
        for bj in range(3):
            idx = bi*3 + bj
            init_bp = block_par[idx]
            bm = {}  # map r_mask to list of (c_mask_global, weight)
            # enumerate flips in 3x3 block
            for m in range(1<<9):
                w = popcount(m)
                if (w & 1) != init_bp:
                    continue
                # compute r_mask (3 bits) and c_mask (3 bits)
                r = 0
                c = 0
                for p in range(9):
                    if not (m >> p) & 1:
                        continue
                    i_off, j_off = divmod(p, 3)
                    r |= 1 << i_off
                    c |= 1 << j_off
                # global col mask for this block
                c_glob = 0
                for j_off in range(3):
                    if (c >> j_off) & 1:
                        c_glob |= 1 << (3*bj + j_off)
                # record
                bm.setdefault(r, []).append((c_glob, w))
            block_masks[bi][bj] = bm
    # For each band, compute minimal flips for each col parity delta
    band_dp = []  # list of dict: col_mask -> min flips
    for bi in range(3):
        # target row parity for this band's rows
        targ_r = 0
        for i in range(3):
            if row_par[3*bi + i]:
                targ_r |= 1 << i
        # maps col_mask to min flips
        cost_map = {}
        bm0 = block_masks[bi][0]
        bm1 = block_masks[bi][1]
        bm2 = block_masks[bi][2]
        # iterate mask0 and mask1
        for r0, lst0 in bm0.items():
            for c0, w0 in lst0:
                for r1, lst1 in bm1.items():
                    for c1, w1 in lst1:
                        r01 = r0 ^ r1
                        # compute required r2
                        r2 = targ_r ^ r01
                        if r2 not in bm2:
                            continue
                        for c2, w2 in bm2[r2]:
                            c_all = c0 ^ c1 ^ c2
                            w_all = w0 + w1 + w2
                            if c_all not in cost_map or w_all < cost_map[c_all]:
                                cost_map[c_all] = w_all
        band_dp.append(cost_map)
    # DP over 3 bands for column parity
    # dp[cur_col_mask] = min flips so far
    dp = {0: 0}
    for bi in range(3):
        new_dp = {}
        cmap = band_dp[bi]
        for prev_c, prev_w in dp.items():
            for dc, w in cmap.items():
                nc = prev_c ^ dc
                nw = prev_w + w
                if nc not in new_dp or nw < new_dp[nc]:
                    new_dp[nc] = nw
        dp = new_dp
    # target column parity mask
    targ_c = 0
    for j in range(9):
        if col_par[j]:
            targ_c |= 1 << j
    # result
    res = dp.get(targ_c, -1)
    print(res)

if __name__ == '__main__':
    main()
