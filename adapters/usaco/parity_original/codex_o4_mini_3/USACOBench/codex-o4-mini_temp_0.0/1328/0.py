#!/usr/bin/env python3
import sys

def main():
    t = sys.stdin.readline().strip()
    n = len(t)
    # Constants
    INF = n

    # Precompute next occurrences for needed chars: b, e, s, i
    next_b = [INF] * (n + 1)
    next_e = [INF] * (n + 1)
    next_s = [INF] * (n + 1)
    next_i = [INF] * (n + 1)
    for idx in range(n - 1, -1, -1):
        # Copy from next position
        next_b[idx] = next_b[idx + 1]
        next_e[idx] = next_e[idx + 1]
        next_s[idx] = next_s[idx + 1]
        next_i[idx] = next_i[idx + 1]
        # Update if match
        c = t[idx]
        if c == 'b': next_b[idx] = idx
        elif c == 'e': next_e[idx] = idx
        elif c == 's': next_s[idx] = idx
        elif c == 'i': next_i[idx] = idx

    # e1[i]: end position of first 'bessie' starting at i, or INF
    e1 = [INF] * n
    for i in range(n):
        # Match 'b'
        p = next_b[i]
        if p == INF:
            continue
        # Match 'e'
        p = next_e[p + 1] if p + 1 <= n else INF
        if p == INF:
            continue
        # Match 's'
        p = next_s[p + 1] if p + 1 <= n else INF
        if p == INF:
            continue
        # Match second 's'
        p = next_s[p + 1] if p + 1 <= n else INF
        if p == INF:
            continue
        # Match 'i'
        p = next_i[p + 1] if p + 1 <= n else INF
        if p == INF:
            continue
        # Match final 'e'
        p = next_e[p + 1] if p + 1 <= n else INF
        if p == INF:
            continue
        e1[i] = p

    # DP for count and sum of end positions
    cnt = [0] * (n + 1)
    sum_e = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if e1[i] == INF:
            cnt[i] = 0
            sum_e[i] = 0
        else:
            j = e1[i] + 1
            cnt[i] = 1 + cnt[j]
            sum_e[i] = e1[i] + sum_e[j]

    # Compute total over all substrings
    total = 0
    # Using Python int for large values
    for i in range(n):
        total += cnt[i] * n - sum_e[i]
    print(total)


if __name__ == '__main__':
    main()
