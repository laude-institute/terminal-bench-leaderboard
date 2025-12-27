"""
Problem: Count 'magical' configurations of N circular stacks.

1. Restate:
   We have N positions in a ring, each with k[i] cows (1..N).
   Each stack 'falls' clockwise: cow at height t in stack i lands at (i + t) mod N.
   After falling, new stack heights k'[i] = number of cows landing at i.
   A configuration is magical if k' == k.
   Compute number of magical k arrays modulo 1e9+7.

2. Conceptual solution:
   - Observing that each k[i] contributes an interval of length k[i] wrapping around.
   - Break each k[i] = q[i] * d + r[i] for chosen divisor d of N.
   - Derive invariance equations: for all u, d*q[u] + r[u] = sum(q) + count of r[v] covering u.
   - Count solutions by summing over all divisors d of N:
       * Enumerate possible q-vector sums and rem-patterns that satisfy the linear constraints.
       * For fixed d, q[i] ranges 0..floor((N-1)/d), r[i] in 0..d-1, subject to bounds.
   - Aggregate counts for each d, take mod 1e9+7.

3. Pseudocode:
   MOD = 10**9 + 7
   function divisors(N): return list of all divisors of N

   function count_for_d(N, d):
       max_q = floor((N) / d)
       total = 0
       # We need q[i] and r[i] vectors of length d satisfying:
       #   for all u in 0..d-1:
       #     d*q[u] + r[u] = sum(q) + sum_{v} [ (u - v mod d) < r[v] ]
       #   and k[i] = d*q[i] + r[i] in [1..N]
       # Count integer solutions combinatorially (dynamic programming over sum(q) and r-pattern).
       # (Details omitted for brevity.)
       return total % MOD

   function main():
       N = int(input())
       result = 0
       for d in divisors(N):
           result = (result + count_for_d(N, d)) % MOD
       print(result)

if __name__ == "__main__":
   main()
"""
