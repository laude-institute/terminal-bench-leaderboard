"""
Pseudocode for scenic valleys problem:

1. Read N and grid of heights.
2. Create list of all cells (height, x, y), sort ascending by height.
3. Initialize DSU structures for N*N cells: parent, size, hole_flag.
4. Create active[N][N] = False.
5. answer = 0

6. For each (h, x, y) in sorted cells:
     mark active[x][y] = True
     idx = x*N + y
     parent[idx] = idx
     size[idx] = 1
     hole_flag[idx] = False   # assume non-holey initially
     # Union with active neighbors
     for each orthogonal neighbor (nx, ny):
         if in bounds and active[nx][ny]:
             union(idx, nx*N+ny)
     # After merging, get root r
     r = find(idx)
     # Determine if component is holey (requires checking complement connectivity)
     if not hole_flag[r]:
         # Check holeiness for this component
         hole_flag[r] = detect_holey(region_cells at root r)
     # If non-holey, accumulate size
     if not hole_flag[r]:
         answer += size[r]

7. Print answer

Functions:
union(u, v): merge DSU, update size and hole_flag OR of both

detect_holey(cells):
    # Flood-fill complement on full grid using 8-connectivity from outside.
    # Mark reachable inactive cells.
    # If any inactive cell adjacent to region is not reachable from outside,
    # region is holey.
    return True/False
"""
