"""
Problem Solution Pseudocode for Button Press and Room Path Counting

1. Read N, K, Q
2. Read adjacency matrix A (NxN)
3. Precompute all-pairs path counts:
   - Precompute matrix powers A_pow[d] = A^d for d = 0..D_max
   - D_max = K*(K+1)//2  # upper bound on number of moves
4. Compute button sequence counts g[d][b_s][b_t]:
   - For each possible starting button b_s and target b_t, and for each total moves d,
     g[d][b_s][b_t] = number of valid button sequences of length d+1 that start with b_s and end with b_t
   - Use combinatorial DP by splitting sequences into segments between increases of the maximum pressed button.
5. For each query (b_s, s, b_t, t):
   - ans = 0
   - For d in 0..D_max:
       ans += g[d][b_s][b_t] * A_pow[d][s][t]
   - Print ans % MOD

Notes:
- Use modulo arithmetic throughout (MOD = 1e9+7)
- Efficiently compute A_pow using successive multiplications
- Efficiently compute g via nested loops over possible max-up sequences and segment permutations
- Total complexity: O(K^3 * N^3 + Q * D_max)

"""

MOD = 10**9 + 7

# 1. Input parsing
N, K, Q = map(int, input().split())
A = [list(map(int, list(input().strip()))) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 2. Compute D_max = K*(K+1)//2
D_max = K * (K+1) // 2

# 3. Precompute adjacency matrix powers A_pow[d] for d=0..D_max
#    A_pow[0] = identity matrix
#    A_pow[d] = A_pow[d-1] * A
# Placeholder for matrix multiplication function
# def mat_mult(X, Y): ...
# A_pow = [I]
# for d in range(1, D_max+1):
#     A_pow.append(mat_mult(A_pow[-1], A))

# 4. Precompute button sequence counts g[d][b_s][b_t]
# Placeholder for g as 3D list of zeros
# g = [[[0] * (K+1) for _ in range(K+1)] for _ in range(D_max+1)]
# Compute g with combinatorial DP as described

# 5. Answer queries
# for b_s, s, b_t, t in queries:
#     ans = 0
#     for d in range(D_max+1):
#         cnt_buttons = g[d][b_s][b_t]
#         cnt_paths = A_pow[d][s-1][t-1]
#         ans = (ans + cnt_buttons * cnt_paths) % MOD
#     print(ans)

# Note: Implement mat_mult, combinatorial DP for g, and optimize for performance.
