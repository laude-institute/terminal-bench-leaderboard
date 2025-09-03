import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    a = [list(map(int, data[2 + i * N:2 + (i + 1) * N])) for i in range(N)]
    # column prefix sums for quick segment sums
    col_ps = [[0] * N for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            col_ps[i + 1][j] = col_ps[i][j] + a[i][j]

    def can(M):
        # Try all horizontal fence placements via bitmask
        for mask in range(1 << (N - 1)):
            hcuts = mask.bit_count()
            if hcuts > K:
                continue
            # Determine row segments boundaries
            segments = []
            prev = 0
            for i in range(N - 1):
                if (mask >> i) & 1:
                    segments.append((prev, i + 1))
                    prev = i + 1
            segments.append((prev, N))
            seg_count = len(segments)
            # Greedy placement of vertical cuts
            cuts = 0
            acc = [0] * seg_count
            ok = True
            for j in range(N):
                # Check if adding this column exceeds M
                for idx, (r1, r2) in enumerate(segments):
                    s = col_ps[r2][j] - col_ps[r1][j]
                    if s > M:
                        ok = False
                        break
                    if acc[idx] + s > M:
                        # place a vertical cut before column j
                        cuts += 1
                        acc = [0] * seg_count
                        break
                if not ok:
                    break
                # accumulate current column after possible cut
                for idx, (r1, r2) in enumerate(segments):
                    acc[idx] += col_ps[r2][j] - col_ps[r1][j]
                if cuts > K - hcuts:
                    ok = False
                    break
            if ok:
                return True
        return False

    # Binary search on answer
    low = max(max(row) for row in a)
    high = sum(sum(row) for row in a)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)


if __name__ == '__main__':
    main()
