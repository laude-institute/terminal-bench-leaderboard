#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        # only the first room matters
        a1 = int(data[idx])
        idx += n
        # the only losing initial position is 4
        if a1 == 4:
            out.append("Farmer Nhoj")
        else:
            out.append("Farmer John")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
