#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    a = list(map(int, data[1:]))
    # Initial maximum value
    max_a = max(a)
    answer = max_a
    # Maximum possible extra merges ~ log2(N)
    max_add = N.bit_length() + 1
    max_v = max_a + max_add
    # f_prev[i] = rightmost index of segment starting at i reducible to value (v-1)
    f_prev = [-1] * N
    for v in range(1, max_v + 1):
        f_cur = [-1] * N
        has_any = False
        # initial positions with value v
        for i in range(N):
            if a[i] == v:
                f_cur[i] = i
                has_any = True
        # merges from two (v-1) segments
        for i in range(N):
            if f_prev[i] != -1:
                j = f_prev[i] + 1
                if j < N and f_prev[j] != -1:
                    f_cur[i] = f_prev[j]
                    has_any = True
        if not has_any:
            break
        answer = v
        f_prev = f_cur
    sys.stdout.write(str(answer))

if __name__ == '__main__':
    main()
