import sys

def main():
    data = sys.stdin.read().split()
    L, N, rF, rB = map(int, data[:4])
    stops = []
    idx = 4
    for _ in range(N):
        x = int(data[idx]); c = int(data[idx+1]); idx += 2
        stops.append((x, c))
    # Select stops with highest tastiness ahead
    best_stops = []
    max_c = 0
    for x, c in reversed(stops):
        if c > max_c:
            best_stops.append((x, c))
            max_c = c
    best_stops.reverse()
    prev_x = 0
    total = 0
    speed_diff = rF - rB
    for x, c in best_stops:
        dist = x - prev_x
        t = dist * speed_diff
        total += t * c
        prev_x = x
    print(total)

if __name__ == "__main__":
    main()
