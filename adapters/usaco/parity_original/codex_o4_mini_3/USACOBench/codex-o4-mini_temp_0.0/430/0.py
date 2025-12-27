#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    X = int(data[0])
    Y = int(data[1])
    count = 0
    strX = str(X)
    strY = str(Y)
    minL = len(strX)
    maxL = len(strY)
    for L in range(minL, maxL + 1):
        for D in range(10):
            for E in range(10):
                if E == D:
                    continue
                for pos in range(L):
                    # skip if leading digit is zero
                    if pos == 0 and E == 0:
                        continue
                    if pos != 0 and D == 0:
                        continue
                    # build number
                    s = [str(D)] * L
                    s[pos] = str(E)
                    num = int(''.join(s))
                    if X <= num <= Y:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()
