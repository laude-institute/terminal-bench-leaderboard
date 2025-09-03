#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    # Read input size
    N = int(next(it))
    # Read preference positions
    pos = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            gift = int(next(it)) - 1
            pos[i][gift] = j
    # Build eligibility bitmask for each cow
    A = [0] * N
    for i in range(N):
        thr = pos[i][i]
        mask = 0
        for j in range(N):
            if pos[i][j] <= thr:
                mask |= 1 << j
        A[i] = mask
    full_mask = (1 << N) - 1
    size = 1 << N
    # DP f[mask]: permanent of A on principal submatrix mask
    f = [0] * size
    f[0] = 1
    for mask in range(1, size):
        # least significant bit as row i
        lowbit = mask & -mask
        i = lowbit.bit_length() - 1
        rem = mask ^ lowbit
        total = 0
        # iterate over possible column j in mask
        poss = mask & A[i]
        while poss:
            lb = poss & -poss
            j = lb.bit_length() - 1
            if j == i:
                prev = rem
            else:
                prev = rem ^ (1 << j)
            total += f[prev]
            poss ^= lb
        f[mask] = total
    # Process queries
    Q = int(next(it))
    out = []
    for _ in range(Q):
        s = next(it).strip()
        m_h = 0
        for idx, ch in enumerate(s):
            if ch == 'H':
                m_h |= 1 << idx
        m_g = full_mask ^ m_h
        # product of matchings for each breed group
        out.append(str(f[m_h] * f[m_g]))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
