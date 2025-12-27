#!/usr/bin/env python3
# Restate the problem:
# Two barns start with 1000 gallons each and sets of buckets.
# Over four days, milk is moved back and forth using a bucket chosen
# from the current barn's buckets. After four moves, compute all
# possible final amounts in barn one.
#
# Conceptual solution:
# Brute-force all sequences of bucket choices over the four moves.
# Update the bucket collections dynamically and compute the net
# milk change. Collect distinct final amounts.
#
# Pseudocode:
# read two lists of bucket sizes for barn1 and barn2
# initialize an empty set 'results'
# for each t_size in barn1:
#   remove t_size from barn1, add to barn2
#   for each w_size in barn2:
#     remove w_size from barn2, add to barn1
#     for each th_size in barn1:
#       remove th_size, add to barn2
#       for each f_size in barn2:
#         compute final = 1000 - t_size + w_size - th_size + f_size
#         add final to results
#       restore barn2, barn1 for next f_size
#     restore after third move
#   restore after second move
# print size of results

import sys

def main():
    data = sys.stdin.read().strip().split()
    b1 = list(map(int, data[:10]))
    b2 = list(map(int, data[10:20]))
    results = set()
    # Tuesday: barn1 -> barn2
    for t in b1:
        b1_t = b1.copy()
        b1_t.remove(t)
        b2_t = b2.copy()
        b2_t.append(t)
        # Wednesday: barn2 -> barn1
        for w in b2_t:
            b2_w = b2_t.copy()
            b2_w.remove(w)
            b1_w = b1_t.copy()
            b1_w.append(w)
            # Thursday: barn1 -> barn2
            for th in b1_w:
                b1_th = b1_w.copy()
                b1_th.remove(th)
                b2_th = b2_w.copy()
                b2_th.append(th)
                # Friday: barn2 -> barn1
                for f in b2_th:
                    # compute final amount in barn1
                    final = 1000 - t + w - th + f
                    results.add(final)
    print(len(results))

if __name__ == '__main__':
    main()
