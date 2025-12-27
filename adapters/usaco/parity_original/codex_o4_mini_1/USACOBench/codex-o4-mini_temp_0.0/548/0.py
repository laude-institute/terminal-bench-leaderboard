def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = [list(next(it).strip()) for _ in range(n)]

    # DP from start to middle
    dp1 = {(0, 0): {grid[0][0]}}
    for step in range(1, n):
        new_dp = {}
        for i in range(n):
            j = step - i
            if j < 0 or j >= n:
                continue
            s = set()
            if (i-1, j) in dp1:
                for st in dp1[(i-1, j)]:
                    s.add(st + grid[i][j])
            if (i, j-1) in dp1:
                for st in dp1[(i, j-1)]:
                    s.add(st + grid[i][j])
            if s:
                new_dp[(i, j)] = s
        dp1 = new_dp

    # DP from end to middle
    dp2 = {(n-1, n-1): {grid[n-1][n-1]}}
    for step in range(1, n):
        new_dp = {}
        sum_idx = 2*(n-1) - step
        for i in range(n):
            j = sum_idx - i
            if j < 0 or j >= n:
                continue
            s = set()
            if (i+1, j) in dp2:
                for st in dp2[(i+1, j)]:
                    s.add(grid[i][j] + st)
            if (i, j+1) in dp2:
                for st in dp2[(i, j+1)]:
                    s.add(grid[i][j] + st)
            if s:
                new_dp[(i, j)] = s
        dp2 = new_dp

    # Count distinct palindromes
    pal_half = set()
    for pos, pre_set in dp1.items():
        suf_set = dp2.get(pos, set())
        rev_suf = {s[::-1] for s in suf_set}
        # common halves
        common = pre_set & rev_suf
        pal_half.update(common)

    print(len(pal_half))


if __name__ == "__main__":
    main()
