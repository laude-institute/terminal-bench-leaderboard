#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0].strip()
    n = len(s)
    # prefix parity sums for C, O, W
    pre = [[0]*(n+1) for _ in range(3)]  # 0:C,1:O,2:W
    mapping = {'C':0, 'O':1, 'W':2}
    for i, ch in enumerate(s, start=1):
        for j in range(3):
            pre[j][i] = pre[j][i-1]
        pre[mapping[ch]][i] ^= 1
    q = int(data[1])
    ans = []
    idx = 2
    for _ in range(q):
        l = int(data[idx]); r = int(data[idx+1]); idx += 2
        # compute parity in substring [l..r]
        c_par = pre[0][r] ^ pre[0][l-1]
        o_par = pre[1][r] ^ pre[1][l-1]
        w_par = pre[2][r] ^ pre[2][l-1]
        # reachable if parity matches final [1,0,0] or [0,1,1]
        if (c_par == 1 and o_par == 0 and w_par == 0) or (c_par == 0 and o_par == 1 and w_par == 1):
            ans.append('Y')
        else:
            ans.append('N')
    sys.stdout.write(''.join(ans))

if __name__ == '__main__':
    main()
