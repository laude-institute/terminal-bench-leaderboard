#!/usr/bin/env python3
import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    N_line = input()
    if not N_line:
        return
    N = int(N_line)
    a = list(map(int, input().split()))
    # Sorted milk values and prefix sums
    S = sorted(a)
    P = [0] * (N + 1)
    for i in range(N):
        P[i+1] = P[i] + S[i]
    # Original total T
    T = 0
    for idx, v in enumerate(S, start=1):
        T += idx * v
    # Process queries
    Q = int(input())
    out_lines = []
    for _ in range(Q):
        i_str, j_str = input().split()
        i = int(i_str) - 1
        v_new = int(j_str)
        v_old = a[i]
        # Find old and new positions (1-based)
        pos_old = bisect_left(S, v_old) + 1
        pos_new = bisect_left(S, v_new) + 1
        # Compute new total based on cases
        if pos_new <= pos_old:
            res = T - pos_old * v_old + P[pos_old-1] + pos_new * v_new - P[pos_new-1]
        else:
            res = T - (pos_old-1) * v_old + P[pos_old-1] + (pos_new-1) * v_new - P[pos_new-1]
        out_lines.append(str(res))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
