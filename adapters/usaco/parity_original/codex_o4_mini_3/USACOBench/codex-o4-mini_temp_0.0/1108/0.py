import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    occupied = set()
    comfortable = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0

    for _ in range(N):
        x, y = map(int, input().split())
        occupied.add((x, y))

        to_check = [(x, y)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in occupied:
                to_check.append((nx, ny))

        for cx, cy in to_check:
            adj = 0
            for dx, dy in directions:
                if (cx + dx, cy + dy) in occupied:
                    adj += 1

            if adj == 3:
                if (cx, cy) not in comfortable:
                    comfortable.add((cx, cy))
                    count += 1
            else:
                if (cx, cy) in comfortable:
                    comfortable.remove((cx, cy))
                    count -= 1

        sys.stdout.write(str(count) + "\n")

if __name__ == "__main__":
    main()
