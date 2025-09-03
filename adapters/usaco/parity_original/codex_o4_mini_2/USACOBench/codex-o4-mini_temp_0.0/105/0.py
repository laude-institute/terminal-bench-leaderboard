#!/usr/bin/env python3
import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    K = int(data[0])
    blocked = [[False]*5 for _ in range(5)]
    idx = 1
    for _ in range(K):
        i = int(data[idx]) - 1; j = int(data[idx+1]) - 1
        blocked[i][j] = True
        idx += 2
    total_grass = 25 - K
    # visited grid marks consumed grass
    visited = [[False]*5 for _ in range(5)]
    # Starting positions: Bessie at (0,0), Mildred at (4,4)
    visited[0][0] = True
    visited[4][4] = True
    # Movement directions
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    count = 0

    def dfs(bi, bj, mi, mj, visited_count):
        nonlocal count
        # If all grass consumed, check meeting
        if visited_count == total_grass:
            if bi == mi and bj == mj:
                count += 1
            return
        # Try all moves for both cows
        for db in dirs:
            nb_r, nb_c = bi + db[0], bj + db[1]
            # Check Bessie's move
            if not (0 <= nb_r < 5 and 0 <= nb_c < 5):
                continue
            if blocked[nb_r][nb_c] or visited[nb_r][nb_c]:
                continue
            for dm in dirs:
                nm_r, nm_c = mi + dm[0], mj + dm[1]
                # Check Mildred's move
                if not (0 <= nm_r < 5 and 0 <= nm_c < 5):
                    continue
                if blocked[nm_r][nm_c] or visited[nm_r][nm_c]:
                    continue
                # Both move to same square: only allowed as final move
                if nb_r == nm_r and nb_c == nm_c:
                    if visited_count + 1 != total_grass:
                        continue
                    visited[nb_r][nb_c] = True
                    dfs(nb_r, nb_c, nm_r, nm_c, visited_count + 1)
                    visited[nb_r][nb_c] = False
                else:
                    # Normal distinct moves
                    visited[nb_r][nb_c] = True
                    visited[nm_r][nm_c] = True
                    dfs(nb_r, nb_c, nm_r, nm_c, visited_count + 2)
                    visited[nb_r][nb_c] = False
                    visited[nm_r][nm_c] = False

    dfs(0, 0, 4, 4, 2)
    print(count)

if __name__ == "__main__":
    main()
