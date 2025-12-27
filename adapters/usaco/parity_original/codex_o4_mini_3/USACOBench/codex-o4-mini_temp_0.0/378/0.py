"""
Pseudocode solution for USACO 'Balanced Teams'

1. Restate the problem:
   Given 12 integer skill levels, form 4 teams of 3 cows each,
   so that the maximum team sum minus the minimum team sum is minimized.

2. Conceptual solution:
   - Perform a depth-first search (DFS) to assign cows into 4 triples.
   - Track which cows are used and the current min/max team sums.
   - Prune search branches where current range >= best found.
   - Update global best difference when 4 teams are formed.

3. Pseudocode:
   skills = read 12 integers
   sort(skills)
   best_diff = infinity
   used = [False] * 12

   function dfs(team_idx, current_min, current_max):
       if team_idx == 4:
           best_diff = min(best_diff, current_max - current_min)
           return
       if current_max - current_min >= best_diff:
           return  # prune

       for i from 0 to 11:
           if used[i]: continue
           used[i] = True
           for j from i+1 to 11:
               if used[j]: continue
               used[j] = True
               for k from j+1 to 11:
                   if used[k]: continue
                   used[k] = True
                   team_sum = skills[i] + skills[j] + skills[k]
                   new_min = team_sum if team_idx == 0 else min(current_min, team_sum)
                   new_max = team_sum if team_idx == 0 else max(current_max, team_sum)
                   dfs(team_idx+1, new_min, new_max)
                   used[k] = False
               used[j] = False
           used[i] = False

   dfs(0, infinity, -infinity)
   print(best_diff)
"""
