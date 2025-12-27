#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    from bisect import bisect_left

    data = sys.stdin.read().split()
    l, r, m = map(int, data[:3])
    ops = []  # list of (char_idx, replacement_str)
    idx = 3
    for _ in range(m):
        c = data[idx]; s = data[idx+1]
        ops.append((ord(c) - 97, s))
        idx += 2

    # Precompute for each char the op positions and corresponding lengths
    INF = 10**18
    cur_len = [1] * 26
    temp_pos = [[] for _ in range(26)]
    temp_len = [[] for _ in range(26)]
    # Process operations in reverse to compute lengths
    for i in range(m, 0, -1):
        c_idx, s = ops[i-1]
        total = 0
        for ch in s:
            total += cur_len[ord(ch) - 97]
            if total > INF:
                total = INF
        cur_len[c_idx] = total
        temp_pos[c_idx].append(i)
        temp_len[c_idx].append(total)
    # Reverse to ascending order
    ops_list = []  # positions per char
    len_list = []  # lengths per char
    for c in range(26):
        ops_list.append(list(reversed(temp_pos[c])))
        len_list.append(list(reversed(temp_len[c])))

    # Helper to get next op index >= stage for a char
    def get_next_op(ch, stage):
        lst = ops_list[ch]
        i = bisect_left(lst, stage)
        return lst[i] if i < len(lst) else None

    # Helper to get length of char expansion at a given stage
    def get_len(ch, stage):
        lst = ops_list[ch]
        ll = len_list[ch]
        i = bisect_left(lst, stage)
        return ll[i] if i < len(lst) else 1

    sys.setrecursionlimit(1000000)
    # Recursive function to extract substring of expansion
    def dfs(stage, ch, l0, r0):
        if l0 > r0:
            return ''
        nxt = get_next_op(ch, stage)
        # If no further replacement, base char
        if nxt is None:
            if l0 <= 1 <= r0:
                return chr(ch + 97)
            return ''
        # Expand at the next operation
        j = nxt
        _, s = ops[j-1]
        res = []
        prefix = 0
        for ch2 in s:
            idx2 = ord(ch2) - 97
            seg_len = get_len(idx2, j+1)
            # Skip segment if before l0
            if prefix + seg_len < l0:
                prefix += seg_len
                continue
            # Stop if past r0
            if prefix + 1 > r0:
                break
            nl = max(1, l0 - prefix)
            nr = min(seg_len, r0 - prefix)
            res.append(dfs(j+1, idx2, nl, nr))
            prefix += seg_len
        return ''.join(res)

    # Compute and output result
    result = dfs(1, 0, l, r)
    sys.stdout.write(result)

if __name__ == '__main__':
    main()
