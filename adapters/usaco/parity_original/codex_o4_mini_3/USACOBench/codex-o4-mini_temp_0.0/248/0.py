"""
Problem 2: Taxi

1. Restate in plain English:
   Bessie starts at 0 on a fence of length M and must end at M. There are N cows, each waiting at position s_i
   and wanting to go to t_i. Bessie can carry one cow at a time, picking up and dropping off instantly.
   We need the minimum distance Bessie must drive (including empty moves and with possible intermediate drop-offs).

2. Conceptual solution in plain English:
   - Represent the fence as a line from 0 to M. Each cow trip is an interval [s_i, t_i] (direction matters).
   - Bessie's route consists of segments carrying a cow and segments empty. We want to minimize empty travel.
   - Model as a minimum-cost flow on a line graph of event points (all unique s_i and t_i, plus 0 and M).
     * Nodes are sorted unique positions.
     * Add edges between consecutive nodes with infinite capacity and cost equal to distance (empty movement).
     * For each cow, add an edge from s_i to t_i with capacity=1 and cost=|s_i - t_i| (carrying movement).
     * Add source at node 0 with supply=N and sink at node M with demand=N.
     * Run min-cost max-flow to send N units; total cost is the answer.

3. Pseudocode:
   read N, M
   trips = []
   positions = {0, M}
   for i in 1..N:
       read s, t
       trips.append((s, t))
       positions.add(s)
       positions.add(t)
   sort positions into list P
   map each pos in P to index
   build graph G with nodes 0..len(P)-1
   for i in 0..len(P)-2:
       u = i, v = i+1, d = P[v] - P[u]
       add_edge(G, u, v, cap=INF, cost=d)
       add_edge(G, v, u, cap=INF, cost=d)
   for each (s, t) in trips:
       u = idx[s], v = idx[t]
       add_edge(G, u, v, cap=1, cost=abs(t - s))
   add source S, sink T
   add_edge(G, S, idx[0], cap=N, cost=0)
   add_edge(G, idx[M], T, cap=N, cost=0)
   answer = min_cost_max_flow(G, S, T, flow=N)
   print(answer)
"""
