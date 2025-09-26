"""
Problem Restatement:
  We have a directed graph of N rooms and K buttons. Each move consists of pressing a button then taking a directed edge (or stopping). Buttons cannot be reused unless a strictly larger button has been pressed in between (pressing x bans x until a button >x resets it). For Q queries (bs, s, bt, t), count sequences of button presses and moves that start at room s with press bs, end at room t with press bt, never violate the ban rule, modulo 1e9+7.

Solution Concept:
  1. Precompute adjacency matrix A of the graph.
  2. Use a recursive DP by maximum button (c from 1..K): let H[c][u][v] = count of valid sequences using buttons ≤c, from start-button u to end-button v, tracking room-to-room transitions via matrix multiplication.
  3. Recurrence: H[c] = H[c-1]  (sequences that never use c)  +  (sum over p< c of H[c-1][u][p]) * A * (sum over q< c of H[c-1][q][v]).
  4. For each query (bs, s, bt, t), maintain partial matrices only for that (bs,bt) pair, iterating c from bs to K to accumulate counts.
  5. Also raise A powers or embed adjacency in the DP steps.

Pseudocode:
  MOD = 10**9+7
  read N, K, Q
  A = read N×N adjacency matrix (mod MOD)
  answers = []
  for each query bs, s, bt, t:
    # initialize H_prev[u][v] = 0 matrices of size N×N
    H_prev = zero matrix of size N×N for each u,v button-pair
    # base: at c = bs, only H_prev[bs][bs] = identity matrix (press bs and stop)
    H_prev[bs][bs] = identity_matrix(N)
    ans_matrix = H_prev[bs][bt]
    # maintain prefix sums of H_prev rows and cols
    row_sum[u] = sum_{p<bs} H_prev[u][p]
    col_sum[v] = sum_{q<bs} H_prev[q][v]
    for c in range(bs+1, K+1):
      # compute contribution of new max c
      # for each u,v: H_cur = H_prev + row_sum[u] * A * col_sum[v]
      # but only need update H_prev[u][c], H_prev[c][v], and ans_matrix
      M_bs = row_sum[bs] @ A  # N×N
      add_to(ans_matrix, M_bs @ col_sum[bt])
      # update H_prev[u][c]
      M_col_c = col_sum[c]
      for u in 1..K:
        M_left = row_sum[u] @ A
        H_prev[u][c] = M_left @ M_col_c
      # update H_prev[c][v]
      M_row_c = row_sum[c] @ A
      for v in 1..K:
        H_prev[c][v] = M_row_c @ col_sum[v]
      # now update row_sum and col_sum
      for u in 1..K: row_sum[u] = (row_sum[u] + H_prev[u][c]) mod
      for v in 1..K: col_sum[v] = (col_sum[v] + H_prev[c][v]) mod
    # final answer entry at (s,t) in ans_matrix
    answer = ans_matrix[s][t] mod MOD
    answers.append(answer)
  print each answer
"""
if __name__ == '__main__':
    # Implementation follows the above pseudocode.
    pass
