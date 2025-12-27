"""
Problem Restatement:
Given an N x N grid of nonnegative integers (cows per pasture), place up to K full horizontal or vertical fences (cuts between rows or columns) to partition the grid into rectangular regions. Minimize the maximum sum of values in any region.

Conceptual Solution:
1. Binary search on the answer M (smallest possible largest-region sum).
2. For a candidate M, check feasibility:
   a. Enumerate all ways to place horizontal cuts (subset of the N-1 possible cuts).
   b. For each horizontal partition (h cuts), greedily place vertical cuts: sweep columns, accumulate per-segment sums, cut when any segment would exceed M.
   c. If total cuts (h + required vertical cuts) <= K, M is feasible.
3. Use prefix sums over rows for fast per-segment column sums.
4. Binary search range: low=max(cell value), high=total sum.

Pseudocode:
read N, K
read grid[N][N]
compute rowPrefix[r+1][c] = sum(grid[0..r][c]) for all r,c
define function feasible(M):
  for mask in [0..(1<<(N-1))-1]:
    h = popcount(mask)
    if h > K: continue
    determine row segments from mask
    compute segSum[s][c] = rowPrefix[end][c] - rowPrefix[start][c]
    for each segment s and column c: if segSum[s][c] > M: skip mask
    cuts = 0; currSum[s]=0 for each segment
    for c in 0..N-1:
      for s: if currSum[s] + segSum[s][c] > M: need cut before c; break
      if cut needed:
        cuts += 1; reset currSum to segSum[*][c]
        if cuts > K - h: break mask
      else:
        add segSum[*][c] to currSum[*]
    if cuts <= K-h: return True
  return False

lo = max cell
hi = total sum
while lo < hi:
  mid = (lo+hi)//2
  if feasible(mid): hi = mid
  else: lo = mid+1
print(lo)
"""

import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    vals = list(map(int, data[2:]))
    grid = [vals[i*N:(i+1)*N] for i in range(N)]

    # Prefix sums over rows: rowPrefix[r][c] = sum of grid[0..r-1][c]
    rowPrefix = [[0]*N for _ in range(N+1)]
    for r in range(N):
        for c in range(N):
            rowPrefix[r+1][c] = rowPrefix[r][c] + grid[r][c]

    total = sum(vals)
    lo = max(vals)
    hi = total

    # Check if we can partition with max region sum <= M
    def feasible(M):
        # iterate horizontal cut masks
        for mask in range(1<<(N-1)):
            h = mask.bit_count()
            if h > K:
                continue

            # build segments: each as [start_row, end_row)
            seg_bounds = []
            start = 0
            for i in range(N-1):
                if mask & (1<<i):
                    seg_bounds.append((start, i+1))
                    start = i+1
            seg_bounds.append((start, N))
            S = len(seg_bounds)

            # segSum[s][c] for each segment and column
            segSum = [[0]*N for _ in range(S)]
            ok = True
            for s, (a, b) in enumerate(seg_bounds):
                for c in range(N):
                    ssum = rowPrefix[b][c] - rowPrefix[a][c]
                    if ssum > M:
                        ok = False; break
                    segSum[s][c] = ssum
                if not ok:
                    break
            if not ok:
                continue

            cuts = 0
            curr = [0]*S
            for c in range(N):
                # check if adding this column exceeds M
                need_cut = False
                for s in range(S):
                    if curr[s] + segSum[s][c] > M:
                        need_cut = True
                        break
                if need_cut:
                    cuts += 1
                    curr = segSum_copy = segSum  # reset to this column sums
                    curr = [segSum[s][c] for s in range(S)]
                    if cuts > K - h:
                        ok = False; break
                else:
                    for s in range(S):
                        curr[s] += segSum[s][c]
            if ok and cuts <= K - h:
                return True
        return False

    # binary search
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == '__main__':
    main()
