#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    S = list(map(int, data[1:]))
    S.sort(reverse=True)
    total = sum(S)
    barns = [0, 0, 0]

    def dfs(index, current_best):
        if index == n:
            return max(barns)
        s = S[index]
        best_local = current_best
        for i in range(3):
            # prune if this barn would exceed current best
            if barns[i] + s > best_local:
                continue
            # skip symmetric assignments
            if i > 0 and barns[i] == barns[i-1]:
                continue
            barns[i] += s
            candidate = dfs(index + 1, best_local)
            if candidate < best_local:
                best_local = candidate
            barns[i] -= s
        return best_local

    result = dfs(0, total)
    print(result)

if __name__ == "__main__":
    main()
