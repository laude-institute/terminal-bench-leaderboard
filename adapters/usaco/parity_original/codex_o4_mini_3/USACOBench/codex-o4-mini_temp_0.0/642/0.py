"""
Restatement:
Given N distinct points on a 2D plane, remove up to three points to minimize
the area of the smallest axis-aligned rectangle that encloses all remaining points.

Conceptualization:
- Only points on the extreme boundaries (smallest/largest x or y) can affect the area.
- Collect a small candidate set of boundary points by sorting by x and y.
- Try removing every combination of up to three candidates.
- For each removal subset, compute remaining min/max x and y to get area.
- Track the minimum area found.

Pseudocode:
1. Read integer N and list of points.
2. Assign each point an index for identification.
3. Sort points by x-coordinate, and separately by y-coordinate.
4. Collect candidate indices: first 4 and last 4 from both sorted lists.
5. Initialize best_area to infinity.
6. For k in 0 to 3:
     For each subset of size k from candidates:
         Mark removed indices.
         Determine min_x = minimum x among unremoved points.
         Determine max_x = maximum x among unremoved points.
         Determine min_y = minimum y among unremoved points.
         Determine max_y = maximum y among unremoved points.
         Compute area = (max_x - min_x) * (max_y - min_y).
         Update best_area if smaller.
7. Print best_area.
"""

def main():
    # Implementation would follow the above pseudocode using only built-in structures
    pass

if __name__ == '__main__':
    main()
