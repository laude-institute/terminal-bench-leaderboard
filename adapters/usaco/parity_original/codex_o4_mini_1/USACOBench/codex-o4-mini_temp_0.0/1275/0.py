#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    s = next(it).strip()
    E = [0] + [int(next(it)) for _ in range(n)]
    G_positions = []
    H_positions = []
    for i, ch in enumerate(s, start=1):
        if ch == 'G':
            G_positions.append(i)
        else:
            H_positions.append(i)
    # first and last positions for each breed
    G1 = G_positions[0]
    H1 = H_positions[0]
    lastG = G_positions[-1]
    lastH = H_positions[-1]
    fullCoverG = (E[G1] >= lastG)
    fullCoverH = (E[H1] >= lastH)
    # raw counts
    raw_count1 = 0
    for h in H_positions:
        if h <= G1 <= E[h]:
            raw_count1 += 1
    H1_in_X = (H1 <= G1 <= E[H1])
    s1 = raw_count1 + (1 if fullCoverH else 0) - (1 if fullCoverH and H1_in_X else 0)
    raw_count2 = 0
    for g in G_positions:
        if g <= H1 <= E[g]:
            raw_count2 += 1
    G1_in_Y = (G1 <= H1 <= E[G1])
    s2 = raw_count2 + (1 if fullCoverG else 0) - (1 if fullCoverG and G1_in_Y else 0)
    # compute overlap
    A_G1 = fullCoverG or (G1 <= H1 <= E[G1])
    B_H1 = fullCoverH or (H1 <= G1 <= E[H1])
    overlap = 1 if (A_G1 and B_H1) else 0
    ans = s1 + s2 - overlap
    print(ans)

if __name__ == '__main__':
    main()
