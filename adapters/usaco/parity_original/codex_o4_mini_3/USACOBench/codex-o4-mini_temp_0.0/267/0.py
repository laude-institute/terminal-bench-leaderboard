#!/usr/bin/env python3
import sys

def main():
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    N, M = len(S), len(T)

    # Build prefix function for T
    pi = [0] * M
    for i in range(1, M):
        j = pi[i-1]
        while j > 0 and T[i] != T[j]:
            j = pi[j-1]
        if T[i] == T[j]:
            j += 1
        pi[i] = j

    # Build automaton next_state: state j with char c leads to next_state[j][c]
    # States are 0..M-1, we forbid reaching state M
    next_state = [[0] * 26 for _ in range(M)]
    for j in range(M):
        for c in range(26):
            ch = chr(ord('a') + c)
            if j > 0 and ch != T[j]:
                next_state[j][c] = next_state[pi[j-1]][c]
            else:
                next_state[j][c] = j + 1 if ch == T[j] else (0 if j == 0 else next_state[pi[j-1]][c])

    INF = N + 5
    # dp_prev[j]: min deletions after processing i chars, with current automaton state j
    dp_prev = [INF] * M
    dp_prev[0] = 0

    for i in range(N):
        c_idx = ord(S[i]) - ord('a')
        dp_cur = [INF] * M
        for j in range(M):
            cost = dp_prev[j]
            if cost >= INF:
                continue
            # Option 1: delete S[i]
            if cost + 1 < dp_cur[j]:
                dp_cur[j] = cost + 1
            # Option 2: keep S[i]
            nj = next_state[j][c_idx]
            if nj < M and cost < dp_cur[nj]:
                dp_cur[nj] = cost
        dp_prev = dp_cur

    # Answer is min deletions over all valid end states
    ans = min(dp_prev)
    print(ans)

if __name__ == '__main__':
    main()
