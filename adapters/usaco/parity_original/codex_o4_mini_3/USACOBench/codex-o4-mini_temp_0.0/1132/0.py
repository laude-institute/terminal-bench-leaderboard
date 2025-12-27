#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    # Read number of publications K and number of members N
    K, N = map(int, input().split())
    # Read member names
    names = input().split()
    # Map each name to its index
    name_to_idx = {name: i for i, name in enumerate(names)}

    # adj[i][j] is True if member i is definitely more senior than member j
    adj = [[False] * N for _ in range(N)]

    # Process each publication
    for _ in range(K):
        order = input().split()
        # For each pair where one appears before another
        for p in range(N):
            ni = order[p]
            for q in range(p + 1, N):
                nj = order[q]
                # If ni > nj lexicographically, then to appear before, ni must have put more effort
                # and cannot be more senior than nj, so nj is more senior than ni
                if ni > nj:
                    u = name_to_idx[nj]
                    v = name_to_idx[ni]
                    adj[u][v] = True

    # Compute transitive closure of seniority relations
    for k in range(N):
        for i in range(N):
            if adj[i][k]:
                for j in range(N):
                    if adj[k][j]:
                        adj[i][j] = True

    # Build and print the result matrix
    output = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append('B')
            elif adj[i][j]:
                row.append('1')
            elif adj[j][i]:
                row.append('0')
            else:
                row.append('?')
        output.append(''.join(row))
    print('\n'.join(output))

if __name__ == '__main__':
    main()
