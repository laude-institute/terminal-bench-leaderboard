#!/usr/bin/env python3
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    g = int(next(it))
    # group members and metadata
    groups = []  # list of lists of members
    group_size = [0] * g
    invited_count = [0] * g
    processed = [False] * g
    # cow to groups map
    cow_groups = [[] for _ in range(n+1)]
    for i in range(g):
        s = int(next(it))
        members = []
        for _ in range(s):
            c = int(next(it))
            members.append(c)
            cow_groups[c].append(i)
        groups.append(members)
        group_size[i] = s

    invited = [False] * (n+1)
    dq = deque()
    # start with cow 1
    invited[1] = True
    dq.append(1)
    total_invited = 1

    # BFS propagation
    while dq:
        cow = dq.popleft()
        for gi in cow_groups[cow]:
            if processed[gi]:
                continue
            invited_count[gi] += 1
            # if reached threshold (size-1), invite all remaining
            if invited_count[gi] >= group_size[gi] - 1:
                processed[gi] = True
                for m in groups[gi]:
                    if not invited[m]:
                        invited[m] = True
                        total_invited += 1
                        dq.append(m)

    # output result
    sys.stdout.write(str(total_invited))

if __name__ == '__main__':
    main()
