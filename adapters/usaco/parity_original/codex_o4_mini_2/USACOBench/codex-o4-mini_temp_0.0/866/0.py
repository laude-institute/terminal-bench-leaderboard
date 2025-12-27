# 0.py: Pseudocode solution for the cow evacuation problem

import sys

# Check if a node can be the last to leave by simulating reversed insertion

def can_be_last(v, N, tree, out_edges, in_deg):
    inserted = set([v])
    # insertion indegree is original out-degree
    ins_deg = [len(out_edges[i]) for i in range(N+1)]
    # neighbor_count[i]: number of neighbors of i in inserted set
    neighbor_count = [0] * (N+1)
    for w in tree[v]:
        neighbor_count[w] = 1
    # initial queue: nodes not inserted with ins_deg==0 and neighbor_count==1
    from collections import deque
    queue = deque([u for u in range(1, N+1)
                   if u not in inserted and ins_deg[u]==0 and neighbor_count[u]==1])
    while queue:
        u = queue.popleft()
        inserted.add(u)
        # update neighbors
        for w in tree[u]:
            if w not in inserted:
                neighbor_count[w] += 1
                if neighbor_count[w] == 1 and ins_deg[w] == 0:
                    queue.append(w)
        # update insertion indegree from reversed precedence
        # reversed: for each v->u original, here u->v
        for a in out_edges[u]:
            ins_deg[a] -= 1
            if a not in inserted and ins_deg[a] == 0 and neighbor_count[a] == 1:
                queue.append(a)
    return len(inserted) == N


def main():
    N, M = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        x, y = map(int, sys.stdin.readline().split())
        tree[x].append(y)
        tree[y].append(x)
    # build precedence graph
    out_edges = [[] for _ in range(N+1)]
    in_deg = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        out_edges[a].append(b)
        in_deg[b] += 1
    # detect cycle in precedence graph
    from collections import deque
    dq = deque([i for i in range(1, N+1) if in_deg[i] == 0])
    cnt = 0
    while dq:
        u = dq.popleft()
        cnt += 1
        for v in out_edges[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                dq.append(v)
    if cnt < N:
        # cycle detected
        for _ in range(N): print(0)
        return
    # candidate last cows: sinks in precedence (out_edges empty)
    ans = [0] * (N+1)
    for i in range(1, N+1):
        if len(out_edges[i]) == 0:
            if can_be_last(i, N, tree, out_edges, in_deg):
                ans[i] = 1
    # output
    for i in range(1, N+1):
        print(ans[i])

if __name__ == '__main__':
    main()
