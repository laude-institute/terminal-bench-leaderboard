"""
0.py - Pseudocode solution for the Mirror Field problem

1. Restate Problem:
   Given an N x M grid where each cell contains a '/' or '\' mirror,
   determine the maximum number of reflections a beam of light
   can experience when shot from outside along any row or column.
   If the beam gets trapped in a cycle, report -1 for infinite reflections.

2. Conceptual Solution:
   - Enumerate all possible entry points around the grid edges:
     top edge (downward), bottom edge (upward),
     left edge (rightward), right edge (leftward).
   - For each entry point, simulate the beam path:
     track current position and direction;
     on hitting '/' or '\' mirror, change direction accordingly and count +1 reflection;
     detect revisiting the same (position, direction) state -> infinite loop.
   - Keep the maximum reflections across all entry points;
     if any simulation detects a loop, return -1.

3. Pseudocode:
   read N, M
   read grid as list of strings
   max_reflections = 0
   infinite = false

   define simulate(start_pos, start_dir):
       reflections = 0
       seen = empty set
       pos, dir = start_pos, start_dir
       while pos is inside grid:
           state = (pos, dir)
           if state in seen:
               infinite = true
               return None
           add state to seen
           cell = grid[pos.row][pos.col]
           if cell == '/':
               dir = reflect_slash(dir)
               reflections += 1
           elif cell == '\':
               dir = reflect_backslash(dir)
               reflections += 1
           pos = move_one_step(pos, dir)
       return reflections

   for each entry point (pos, dir):
       result = simulate(pos, dir)
       if infinite:
           print(-1)
           exit
       max_reflections = max(max_reflections, result)

   print(max_reflections)
"""
