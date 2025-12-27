#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.readline().strip()
    memo = {}

    def g(t):
        if t in memo:
            return memo[t]
        n = len(t)
        total = 1  # count empty sequence (no operations)
        # reverse operations only possible if (n+1) is even
        if (n + 1) % 2 == 0:
            m = (n + 1) // 2
            # op1: t = p[1:] + p
            p1 = t[-m:]
            if t[:m-1] == p1[1:]:
                total += g(p1)
            # op2: t = p + p[1:]
            p2 = t[:m]
            if t[m:] == p2[1:]:
                total += g(p2)
            # op3: t = p[:-1] + p
            p3 = t[-m:]
            if t[:m-1] == p3[:-1]:
                total += g(p3)
            # op4: t = p + p[:-1]
            p4 = t[:m]
            if t[m:] == p4[:-1]:
                total += g(p4)
        memo[t] = total
        return total

    # result is total sequences minus the empty one
    result = g(s) - 1
    print(result)

if __name__ == '__main__':
    main()
