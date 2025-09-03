#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    data = input().split()
    if not data:
        return
    K, N = map(int, data)
    names = input().split()
    name_to_idx = {name: i for i, name in enumerate(names)}
    # adjacency matrix: adj[u][v] = True if u is definitely more senior than v
    adj = [[False] * N for _ in range(N)]
    # process each publication
    for _ in range(K):
        pub = input().split()
        # for each pair (i, j) with i before j
        for i in range(N):
            for j in range(i + 1, N):
                name_i = pub[i]
                name_j = pub[j]
                # if name_i > name_j lex, tie would put name_j first, so name_i had more effort
                # more effort => more junior, so name_j is more senior
                if name_i > name_j:
                    u = name_to_idx[name_j]
                    v = name_to_idx[name_i]
                    adj[u][v] = True
    # compute transitive closure (Floyd-Warshall)
    for k in range(N):
        for i in range(N):
            if adj[i][k]:
                for j in range(N):
                    if adj[k][j]:
                        adj[i][j] = True
    # output result matrix
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
        sys.stdout.write(''.join(row) + '\n')

if __name__ == '__main__':
    main()
