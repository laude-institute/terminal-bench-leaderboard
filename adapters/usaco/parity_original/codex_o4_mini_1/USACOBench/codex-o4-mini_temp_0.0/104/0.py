"""
Problem: Haybale Stacking

1. Restate the problem:
   We have N stacks initially height 0. We receive K instructions, each adding +1 haybale to every stack in a given range [A, B].  After all ops, report the median height among all N stacks (N is odd).

2. Conceptual solution:
   Use a difference array of size N+2.  For each instruction [A, B], do diff[A] += 1 and diff[B+1] -= 1.  Then take prefix sums to get final heights for each stack.  Sort heights and pick the middle element as the median.

3. Pseudocode:
   read N, K
   create diff array of length N+2 initialized to 0
   for each of K instructions:
       read A, B
       diff[A] += 1
       diff[B+1] -= 1
   create heights list
   current = 0
   for i from 1 to N:
       current += diff[i]
       append current to heights
   sort heights
   print heights[N//2]
"""

import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    diff = [0] * (N + 2)
    idx = 2
    for _ in range(K):
        A = int(data[idx]); B = int(data[idx+1])
        diff[A] += 1
        diff[B+1] -= 1
        idx += 2

    heights = [0] * N
    curr = 0
    for i in range(1, N+1):
        curr += diff[i]
        heights[i-1] = curr

    heights.sort()
    # N is odd, so middle index is N//2
    print(heights[N//2])

if __name__ == "__main__":
    main()
