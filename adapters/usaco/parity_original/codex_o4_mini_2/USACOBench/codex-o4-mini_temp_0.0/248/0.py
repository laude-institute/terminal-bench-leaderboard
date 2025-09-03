#!/usr/bin/env python3
"""
1. Problem Restatement:
   Bessie has N cows wanting rides along a fence from 0 to M. She starts at 0 and ends at M,
   can carry one cow at a time, and may drop cows temporarily. Minimize total distance driven.

2. Conceptual Solution:
   Only cows needing to move backward (s_i > t_i) force Bessie to backtrack.
   Each backward request defines an interval [t_i, s_i]. Merging these intervals gives
   the total length Bessie must traverse backward. She drives the fence forward once (distance M),
   and backtracks twice the union length of backward intervals.

3. Pseudocode:
   read N, M
   intervals = []
   for each cow:
       if s > t: add (t, s) to intervals
   sort intervals by start
   total_back = 0
   if intervals non-empty:
       cur_start, cur_end = first interval
       for each (start, end) in remaining intervals:
           if start > cur_end:
               total_back += cur_end - cur_start
               cur_start, cur_end = start, end
           else:
               cur_end = max(cur_end, end)
       total_back += cur_end - cur_start
   answer = M + 2 * total_back
   print(answer)
"""

import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    intervals = []
    idx = 2
    for _ in range(N):
        s = int(data[idx]); t = int(data[idx+1]); idx += 2
        if s > t:
            intervals.append((t, s))
    intervals.sort()
    total_back = 0
    if intervals:
        cur_start, cur_end = intervals[0]
        for start, end in intervals[1:]:
            if start > cur_end:
                total_back += cur_end - cur_start
                cur_start, cur_end = start, end
            else:
                if end > cur_end:
                    cur_end = end
        total_back += cur_end - cur_start
    # Total distance = forward once + backtrack twice
    result = M + 2 * total_back
    print(result)

if __name__ == '__main__':
    main()
