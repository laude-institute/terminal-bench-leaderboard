#!/usr/bin/env python3
import sys
import threading

def main():
    import bisect
    from array import array

    INF = 10**18
    data = sys.stdin.read().split()
    l = int(data[0])
    r = int(data[1])
    m = int(data[2])
    ops_c = []  # int 0-25
    ops_s = []  # list of ints
    idx = 3
    idx_list = [[] for _ in range(26)]
    for i in range(m):
        c = data[idx]; s = data[idx+1]
        idx += 2
        ci = ord(c) - 97
        ops_c.append(ci)
        si = [ord(ch) - 97 for ch in s]
        ops_s.append(si)
        idx_list[ci].append(i)

    # len_matrix[i]: lengths after ops i..m-1 for each letter
    len_matrix = [None] * (m+1)
    base = array('Q', [1]) * 26
    len_matrix[m] = base
    # build backwards
    for i in range(m-1, -1, -1):
        prev = len_matrix[i+1]
        curr = array('Q', prev)
        c = ops_c[i]
        total = 0
        for x in ops_s[i]:
            total += prev[x]
            if total >= INF:
                total = INF
                break
        curr[c] = total
        len_matrix[i] = curr

    # iterative expansion
    out = []
    stack = [(-1, ord('a')-97, l, r)]
    while stack:
        i, ch, l0, r0 = stack.pop()
        if l0 > r0:
            continue
        lst = idx_list[ch]
        # find next op > i
        pos = bisect.bisect_right(lst, i)
        if pos == len(lst):
            # no further ops, single char
            if l0 <= 1 <= r0:
                out.append(chr(ch + 97))
            continue
        j = lst[pos]
        pos_acc = 0
        child_segs = []
        for x in ops_s[j]:
            length = len_matrix[j+1][x]
            start = pos_acc + 1
            end = pos_acc + length
            if end >= l0 and start <= r0:
                nl = max(1, l0 - pos_acc)
                nr = min(length, r0 - pos_acc)
                child_segs.append((j, x, nl, nr))
            pos_acc = end
            if pos_acc >= r0:
                break
        # push children in reverse order for correct output
        for seg in reversed(child_segs):
            stack.append(seg)

    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    main()
