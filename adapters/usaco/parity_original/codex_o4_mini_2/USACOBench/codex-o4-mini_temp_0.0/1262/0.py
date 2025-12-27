#!/usr/bin/env python3
import sys

def main():
    S = sys.stdin.readline().strip()
    if not S:
        return
    N = len(S)
    # prefix parity: bits: bit0 for G, bit1 for H
    P = [0] * (N+1)
    for i, c in enumerate(S, 1):
        P[i] = P[i-1] ^ (1 if c=='G' else 2)
    # prefix counts of each parity state
    pref = [[0]*(N+2) for _ in range(4)]
    for i in range(N+1):
        for s in range(4): pref[s][i+1] = pref[s][i]
        pref[P[i]][i+1] += 1
    # positions of G
    Gpos = [i for i,c in enumerate(S) if c=='G']
    M = len(Gpos)
    # D array
    D = [Gpos[t] - t for t in range(M)]
    # prefix sums of D
    Ds = [0]*(M+1)
    for i in range(M): Ds[i+1] = Ds[i] + D[i]
    total = 0
    # sum over ranges of G-index a..b
    for a in range(M):
        # i range [i_lo, i_hi]
        i_lo = Gpos[a-1]+1 if a>0 else 0
        i_hi = Gpos[a]
        I_len = i_hi - i_lo + 1
        # counts of P[i] in i range
        cPi = [0]*4
        for s in range(4):
            cPi[s] = pref[s][i_hi+1] - pref[s][i_lo]
        for b in range(a+1, M):
            # j range [j_lo, j_hi]
            j_lo = Gpos[b]
            j_hi = Gpos[b+1]-1 if b+1<M else N-1
            J_len = j_hi - j_lo + 1
            total_pairs = I_len * J_len
            # counts of P[j+1] over k range [j_lo+1, j_hi+1]
            cPk = [0]*4
            for s in range(4):
                cPk[s] = pref[s][j_hi+2] - pref[s][j_lo+1]
            # invalid where P[i] xor P[j+1] == 3
            invalid_ab = cPi[1]*cPk[2] + cPi[2]*cPk[1] + cPi[0]*cPk[3] + cPi[3]*cPk[0]
            valid = total_pairs - invalid_ab
            if valid <= 0:
                continue
            # cost for G-index range a..b
            m = b - a + 1
            mid = a + (m//2)
            # sum abs D[t] - D[mid] for t in [a..b]
            # left side
            left_cnt = mid - a
            left_sum = Ds[mid] - Ds[a]
            right_sum = Ds[b+1] - Ds[mid+1]
            right_cnt = b - mid
            dmid = D[mid]
            cost = dmid*left_cnt - left_sum + right_sum - dmid*right_cnt
            total += cost * valid
    # count invalid substrings (contribute -1 each)
    cnt = 0
    # total invalid pairs (l<r) where P[l] xor P[r] == 3
    # count pairs unordered
    ct = [pref[s][N+1] for s in range(4)]  # count of P[0..N]
    cnt = ct[1]*ct[2] + ct[0]*ct[3]
    # subtract invalid contributions
    total -= cnt
    print(total)

if __name__ == '__main__':
    main()
