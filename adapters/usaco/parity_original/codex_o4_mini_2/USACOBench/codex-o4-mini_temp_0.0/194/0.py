#!/usr/bin/env python3
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    K = int(next(it))
    N = int(next(it))
    S = [list(next(it).strip()) for _ in range(K)]
    # Compute prefix sums
    P = [[0] * (N + 1) for _ in range(K)]
    for m in range(K):
        for i in range(1, N + 1):
            P[m][i] = P[m][i-1] + (1 if S[m][i-1] == '(' else -1)
    # Stacks for previous smaller prefix index
    stacks = [[0] for _ in range(K)]
    last_sm = [ -1 ] * K
    # Map of vector to count
    count_map = defaultdict(int)
    # Vector list for positions
    V_list = []
    # Initial position 0
    zero_vec = tuple(0 for _ in range(K))
    V_list.append(zero_vec)
    count_map[zero_vec] = 1
    remove_ptr = 0
    ans = 0
    # Iterate over positions 1..N
    for j in range(1, N + 1):
        # Update last_sm for each string
        for m in range(K):
            st = stacks[m]
            while st and P[m][st[-1]] >= P[m][j]:
                st.pop()
            last_sm[m] = st[-1] if st else -1
            st.append(j)
        last_bad = max(last_sm)
        # Current vector
        Vj = tuple(P[m][j] for m in range(K))
        # Remove outdated positions
        while remove_ptr <= last_bad:
            Vold = V_list[remove_ptr]
            count_map[Vold] -= 1
            remove_ptr += 1
        # Count valid substrings ending at j
        ans += count_map.get(Vj, 0)
        # Add current position
        V_list.append(Vj)
        count_map[Vj] += 1
    # Output result
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
