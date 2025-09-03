#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin
    s = data.readline().strip()
    n = len(s)
    # prefix sums for counts of C, O, W
    pc = [0] * (n + 1)
    po = [0] * (n + 1)
    pw = [0] * (n + 1)
    for i, ch in enumerate(s, 1):
        pc[i] = pc[i-1] + (ch == 'C')
        po[i] = po[i-1] + (ch == 'O')
        pw[i] = pw[i-1] + (ch == 'W')
    Q = int(data.readline())
    out = []
    for _ in range(Q):
        l, r = map(int, data.readline().split())
        c = pc[r] - pc[l-1]
        o = po[r] - po[l-1]
        w = pw[r] - pw[l-1]
        # parity condition: target (1,0,0) or (0,1,1)
        if (c % 2 == 1 and o % 2 == 0 and w % 2 == 0) or \
           (c % 2 == 0 and o % 2 == 1 and w % 2 == 1):
            out.append('Y')
        else:
            out.append('N')
    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    main()
