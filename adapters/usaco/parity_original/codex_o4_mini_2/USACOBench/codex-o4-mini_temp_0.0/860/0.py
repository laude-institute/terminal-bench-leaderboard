import sys

def main():
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    lines = data[2:]
    board = [list(map(int, list(line))) for line in lines]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        visited = [[False] * 10 for _ in range(N)]
        to_remove = []
        for i in range(N):
            for j in range(10):
                if board[i][j] != 0 and not visited[i][j]:
                    color = board[i][j]
                    stack = [(i, j)]
                    comp = []
                    visited[i][j] = True
                    while stack:
                        r, c = stack.pop()
                        comp.append((r, c))
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < 10:
                                if not visited[nr][nc] and board[nr][nc] == color:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc))
                    if len(comp) >= K:
                        to_remove.extend(comp)
        if not to_remove:
            break
        for r, c in to_remove:
            board[r][c] = 0
        # Apply gravity
        for j in range(10):
            new_col = [board[i][j] for i in range(N) if board[i][j] != 0]
            zeros = [0] * (N - len(new_col))
            col = zeros + new_col
            for i in range(N):
                board[i][j] = col[i]
    # Output result
    out = sys.stdout
    for row in board:
        out.write(''.join(str(x) for x in row) + '\n')

if __name__ == '__main__':
    main()
