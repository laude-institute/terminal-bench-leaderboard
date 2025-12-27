import sys

def main():
    import sys
    input = sys.stdin.readline
    # Read input
    N, B = map(int, input().split())
    f = list(map(int, input().split()))
    # Prepare tiles sorted by snow depth descending
    tiles = [(f[i], i) for i in range(N)]
    tiles.sort(reverse=True)
    # Read boots with original indices, sorted by max depth descending
    boots = []  # each as (s_i, d_i, original_index)
    for idx in range(B):
        s, d = map(int, input().split())
        boots.append((s, d, idx))
    boots.sort(reverse=True, key=lambda x: x[0])
    # Doubly-linked list via arrays for active tiles
    left = [i - 1 for i in range(N)]
    right = [i + 1 for i in range(N)]
    right[N - 1] = -1
    # Track maximum required step (gap) as we remove tiles
    max_gap = 1
    ans = [0] * B
    ptr = 0
    # Process boots in descending snow tolerance
    for s, d, idx in boots:
        # Remove all tiles with depth > s
        while ptr < N and tiles[ptr][0] > s:
            _, i = tiles[ptr]
            l = left[i]
            r = right[i]
            # Link neighbors to skip removed tile
            if l != -1:
                right[l] = r
            if r != -1:
                left[r] = l
            # Update max gap if interior removal
            if l != -1 and r != -1:
                gap = r - l
                if gap > max_gap:
                    max_gap = gap
            ptr += 1
        # If current largest gap <= boot's max step, it's usable
        ans[idx] = 1 if max_gap <= d else 0
    # Output results in original order
    output = '\n'.join(str(x) for x in ans)
    print(output)

if __name__ == '__main__':
    main()
