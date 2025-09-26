"""
Problem 2: Simplifying the Farm

1. Read N (fields), M (paths)
2. Read M edges (u, v, w)
3. Sort edges by weight w
4. Initialize union-find structure UF for N vertices
5. total_cost = 0
6. total_ways = 1 (mod 1e9+7)

7. For each group of edges with the same weight w:
   a. Collect edges in this group
   b. Identify candidate edges: those whose endpoints lie in different UF components
   c. Determine k = number of edges Kruskal would take from candidates:
      - Copy UF to tempUF
      - For each candidate (u, v) in arbitrary order:
          if tempUF.find(u) != tempUF.find(v):
              tempUF.union(u, v)
              k += 1
   d. Count ways = number of subsets of candidates of size k that form valid unions:
      - For each subset of candidates of size k:
          copy UF to tempUF2
          valid = true
          for (u, v) in subset:
              if tempUF2.find(u) == tempUF2.find(v):
                  valid = false; break
              tempUF2.union(u, v)
          if valid: ways += 1
   e. total_ways = (total_ways * ways) mod 1e9+7
   f. For each candidate (u, v) in increasing order:
         if UF.find(u) != UF.find(v):
             UF.union(u, v)
             total_cost += w

8. Output total_cost and total_ways
"""

def main():
    pass  # implementation based on above pseudocode

if __name__ == '__main__':
    main()
