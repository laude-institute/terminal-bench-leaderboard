#!/usr/bin/env python3
import sys
import threading

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    breeds = data[1].strip()
    E = list(map(int, data[2:2+n]))

    # Collect positions of each breed
    G_pos = []
    H_pos = []
    for i, b in enumerate(breeds, start=1):
        if b == 'G':
            G_pos.append(i)
        else:
            H_pos.append(i)
    # Determine full coverage thresholds
    lastG = G_pos[-1]
    lastH = H_pos[-1]

    # Separate full and non-full cows
    fullG = []        # positions of G cows covering all G
    nonfullG = []     # (pos, Epos) for other G cows
    for pos in G_pos:
        if E[pos-1] >= lastG:
            fullG.append(pos)
        else:
            nonfullG.append((pos, E[pos-1]))
    fullH = []
    nonfullH = []
    for pos in H_pos:
        if E[pos-1] >= lastH:
            fullH.append(pos)
        else:
            nonfullH.append((pos, E[pos-1]))

    # Case 1: both full
    cnt1 = len(fullG) * len(fullH)

    # Case 2: G full, H not full (H must cover gpos)
    from bisect import bisect_left
    H_non_full_E = sorted([eh for _, eh in nonfullH])
    cnt2 = 0
    mHnf = len(H_non_full_E)
    for gpos in fullG:
        idx = bisect_left(H_non_full_E, gpos)
        cnt2 += mHnf - idx

    # Case 3: H full, G not full (G must cover hpos)
    G_non_full_E = sorted([eg for _, eg in nonfullG])
    cnt3 = 0
    mGnf = len(G_non_full_E)
    for hpos in fullH:
        idx = bisect_left(G_non_full_E, hpos)
        cnt3 += mGnf - idx

    # Case 4: neither full (both must cover each other)
    # Count pairs (g,h) where E_g >= hpos and E_h >= gpos
    # Sort nonfull G by E_g, nonfull H by hpos
    nonfullG.sort(key=lambda x: x[1])
    nonfullH.sort(key=lambda x: x[0])
    # BIT for counting H by E_h
    size = n + 2
    bit = [0] * (size)
    def bit_add(i, v):
        while i < size:
            bit[i] += v
            i += i & -i
    def bit_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    cnt4 = 0
    j = 0
    totalHnf = len(nonfullH)
    for gpos, Eg in nonfullG:
        # add H cows with hpos <= Eg
        while j < totalHnf and nonfullH[j][0] <= Eg:
            _, Eh = nonfullH[j]
            bit_add(Eh, 1)
            j += 1
        # count added H with E_h >= gpos
        cnt4 += bit_sum(n) - bit_sum(gpos - 1)

    # Total
    print(cnt1 + cnt2 + cnt3 + cnt4)

if __name__ == '__main__':
    main()
