"""
Problem: Bessie hiking checkpoints 1..N, K tickets.
Each ticket i: purchasable at checkpoint c_i, price p_i, grants access to interval [a_i, b_i].
Starting at checkpoint i (only i is initially accessible), Bessie may buy tickets at any accessible c_j,
expanding accessible set to include [a_j, b_j]. She can move freely among accessible checkpoints.
Goal: for each starting i, find minimum total price to have access to both checkpoints 1 and N.
If impossible, output -1.
"""

def solve():
    # 1. Read N, K and tickets
    N, K = map(int, input().split())
    tickets = []  # list of (c, p, a, b)
    for _ in range(K):
        c, p, a, b = map(int, input().split())
        tickets.append((c, p, a, b))

    # 2. Build adjacency: for each checkpoint, list tickets at that c
    #    and for each ticket, its interval [a, b]
    by_checkpoint = {i: [] for i in range(1, N+1)}
    for idx, (c, p, a, b) in enumerate(tickets):
        by_checkpoint[c].append(idx)

    # 3. For each start i, run Dijkstra on state (pos, mask), mask bits: 1 reaches 1, 2 reaches N
    #    prioritize cost; stop when mask == 3
    import heapq

    def compute_min_cost(start):
        INF = float('inf')
        # dist[(pos, mask)] = min cost
        dist = {}
        initial_mask = 0
        if start == 1: initial_mask |= 1
        if start == N: initial_mask |= 2
        pq = [(0, start, initial_mask)]
        dist[(start, initial_mask)] = 0

        while pq:
            cost, pos, mask = heapq.heappop(pq)
            # if we have both endpoints, done
            if mask == 3:
                return cost
            if dist.get((pos, mask), INF) < cost:
                continue

            # try buying any ticket at pos
            for idx in by_checkpoint.get(pos, []):
                c, p, a, b = tickets[idx]
                new_mask = mask
                if a <= 1 <= b: new_mask |= 1
                if a <= N <= b: new_mask |= 2
                next_cost = cost + p
                # for every checkpoint x in [a, b]: move there with new_mask
                # (movement is free among accessible)
                for x in range(a, b+1):
                    state = (x, new_mask)
                    if dist.get(state, INF) > next_cost:
                        dist[state] = next_cost
                        heapq.heappush(pq, (next_cost, x, new_mask))
        return -1

    # 4. Output answer for each i
    for i in range(1, N+1):
        print(compute_min_cost(i))


if __name__ == '__main__':
    solve()
