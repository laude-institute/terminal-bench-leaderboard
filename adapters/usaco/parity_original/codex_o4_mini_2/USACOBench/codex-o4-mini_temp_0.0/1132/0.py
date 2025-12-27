#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    K = int(next(it))
    N = int(next(it))
    # Read lab member names and build index map
    names = [next(it) for _ in range(N)]
    idx = {name: i for i, name in enumerate(names)}
    # direct[u][v] = True if u is definitely more senior than v
    direct = [[False] * N for _ in range(N)]

    # Process each publication
    for _ in range(K):
        pub = [next(it) for _ in range(N)]
        # For each pair in the author list, infer seniority
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                name_i = pub[i]
                name_j = pub[j]
                # i before j in list => effort(i) >= effort(j)
                if i < j:
                    # if name_i > name_j, alphabetical tie impossible => effort(i) > effort(j)
                    # so i is more junior, j is more senior
                    if name_i > name_j:
                        direct[idx[name_j]][idx[name_i]] = True
                else:
                    # i after j => effort(i) <= effort(j)
                    # if name_i < name_j, tie impossible => effort(i) < effort(j)
                    # so i is more senior than j
                    if name_i < name_j:
                        direct[idx[name_i]][idx[name_j]] = True

    # Compute transitive closure of seniority
    senior = [row[:] for row in direct]
    for k in range(N):
        for i in range(N):
            if senior[i][k]:
                for j in range(N):
                    if senior[k][j]:
                        senior[i][j] = True

    # Build and print output matrix
    out_lines = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append('B')
            elif senior[i][j]:
                row.append('1')
            elif senior[j][i]:
                row.append('0')
            else:
                row.append('?')
        out_lines.append(''.join(row))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
