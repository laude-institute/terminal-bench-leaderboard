#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # variables: B, E, S, I, G, O, M
    vars_vals = {'B': [], 'E': [], 'S': [], 'I': [], 'G': [], 'O': [], 'M': []}
    idx = 1
    for _ in range(n):
        var = data[idx]; val = int(data[idx+1]); idx += 2
        vars_vals[var].append(val)

    # Precompute counts of remainders modulo 7 for each variable
    rem_counts = {}
    for var, vals in vars_vals.items():
        cnt = [0]*7
        for v in vals:
            cnt[v % 7] += 1
        rem_counts[var] = cnt

    # coefficients for each variable in (A, C, D) where:
    # A = B + 2E + 2S + I (mod 7)
    # C = G + O + E + S (mod 7)
    # D = M + 2O (mod 7)
    coeffs = {
        'B': (1, 0, 0),
        'E': (2, 1, 0),
        'S': (2, 1, 0),
        'I': (1, 0, 0),
        'G': (0, 1, 0),
        'O': (0, 1, 2),
        'M': (0, 0, 1),
    }

    # dp[a][c][d] = ways
    # use a dict for sparse representation
    dp = {(0, 0, 0): 1}
    # iterate variables in any order (use defined order)
    order = ['B', 'E', 'S', 'I', 'G', 'O', 'M']
    for var in order:
        cA, cC, cD = coeffs[var]
        cnts = rem_counts[var]
        new_dp = {}
        for (a, c, d), ways in dp.items():
            for r in range(7):
                cnt_r = cnts[r]
                if cnt_r == 0:
                    continue
                na = (a + cA * r) % 7
                nc = (c + cC * r) % 7
                nd = (d + cD * r) % 7
                new_dp[(na, nc, nd)] = new_dp.get((na, nc, nd), 0) + ways * cnt_r
        dp = new_dp

    # sum ways where product A*C*D mod 7 == 0
    total = 0
    for (a, c, d), ways in dp.items():
        if (a * c * d) % 7 == 0:
            total += ways
    print(total)

if __name__ == '__main__':
    main()
