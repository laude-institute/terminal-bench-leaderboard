#!/usr/bin/env python3
# Problem Restatement:
# N cows labeled 1..N in a line. Given M intervals (L_i,R_i), we repeat reversing
# each interval in sequence, and repeat this whole M-step process K times.
# Output the final labels from left to right.
#
# Solution Concept:
# One full M-step process defines a permutation P on positions 0..N-1.
# We compute P by simulating one iteration over an index array.
# Then decompose P into cycles and apply P K times efficiently by
# rotating each cycle by K mod cycle_length.
#
# Pseudocode:
# Read N, M, K
# Read intervals, convert to 0-based
# Initialize pos = [0..N-1]
# For each interval (l,r): reverse pos[l:r+1]
# Build P: for new_pos j, old_i=pos[j], so P[old_i]=j
# Initialize final array of size N
# visited = [False]*N
# For i in range(N):
#     if not visited[i]:
#         build cycle by following P until return
#         for each index in cycle:
#             new_index = cycle[(idx + K)%len(cycle)]
#             final[new_index] = original_label (i+1)
# Print final array one per line
def main():
    import sys

    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    intervals = [tuple(map(int, input().split())) for _ in range(M)]

    # simulate one full process to get permutation P
    pos = list(range(N))
    for l, r in intervals:
        # convert to 0-based
        l -= 1
        r -= 1
        # reverse subarray
        pos[l:r+1] = reversed(pos[l:r+1])

    # build P where P[i] = new position of element originally at i
    P = [0] * N
    for new_j, old_i in enumerate(pos):
        P[old_i] = new_j

    # compute final positions by cycle decomposition
    visited = [False] * N
    result = [0] * N
    for i in range(N):
        if not visited[i]:
            cycle = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = P[cur]
            L = len(cycle)
            shift = K % L
            for idx, u in enumerate(cycle):
                new_pos = cycle[(idx + shift) % L]
                # labels are u+1
                result[new_pos] = u + 1

    # output results
    out = sys.stdout
    for x in result:
        out.write(str(x) + "\n")

if __name__ == "__main__":
    main()
