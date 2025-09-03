"""
Problem Restatement:
We have a boolean array A of length 2N. Bessie's score is the number of inversions (1 before 0) in the first half; Elsie's score is the inversions in the second half. We want the minimum number of adjacent swaps so that the two halves have equal inversion counts.

Solution Concept:
1. Compute initial inversion counts inv_L and inv_R for the two halves, and their difference D = inv_L - inv_R.
2. We have two operations:
   a) Swap adjacent elements within a half: changes the inversion difference by ±1, cost = 1.
   b) Swap across the middle boundary: swapping A[N-1] and A[N] changes D by delta = (A[N-1] - A[N]) * (ones_before - zeros_after), cost = 1.
3. We seek the minimal number of swaps (mix of these operations) to make D = 0.

Pseudocode:
----------------
read N and array A
compute inv_L and inv_R using prefix counts
D = inv_L - inv_R
if D == 0: print(0) and exit

# Greedy approach:
# 1) While abs(D) > 0:
#    - Compute delta for a boundary swap (if A[N-1] != A[N])
#    - If boundary swap helps reduce abs(D) by more than 1, perform it: swap, update D, update ones_before/zeros_after, cost += 1
#    - Else perform an internal half-swap to adjust D by 1: find an adjacent inversion or sorted pair in the appropriate half, swap, update D by ±1, cost += 1
# print cost

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    # TODO: implement above pseudocode
    pass

if __name__ == "__main__":
    main()
"""
