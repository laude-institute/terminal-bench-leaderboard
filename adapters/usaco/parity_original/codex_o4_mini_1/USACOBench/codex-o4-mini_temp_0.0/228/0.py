#!/usr/bin/env python3
"""
Party Invitations (invite)
Given groups of cows with the rule that if all but one cow in a group
are invited, the last one must be invited, determine the minimum number
of cows invited, starting with cow #1.
"""
import sys
from collections import deque

def main():
    data = sys.stdin
    # Read N cows and G groups
    line = data.readline().split()
    N, G = map(int, line)
    # Map cows to the groups they belong to
    cow_to_groups = {}
    # Track remaining uninvited in each group and XOR of remaining
    group_remaining = [0] * G
    group_xor = [0] * G

    # Read group definitions
    for gid in range(G):
        parts = data.readline().split()
        S = int(parts[0])
        members = list(map(int, parts[1:]))
        group_remaining[gid] = S
        x = 0
        for cow in members:
            x ^= cow
            cow_to_groups.setdefault(cow, []).append(gid)
        group_xor[gid] = x

    invited = [False] * (N + 1)
    queue = deque()
    # Start by inviting cow #1
    invited[1] = True
    queue.append(1)
    count = 1

    # BFS-like propagation
    while queue:
        cow = queue.popleft()
        for gid in cow_to_groups.get(cow, []):
            # Mark this cow as processed for the group
            group_remaining[gid] -= 1
            group_xor[gid] ^= cow
            # If only one cow remains uninvited, invite it
            if group_remaining[gid] == 1:
                last = group_xor[gid]
                if not invited[last]:
                    invited[last] = True
                    count += 1
                    queue.append(last)

    # Output result
    sys.stdout.write(str(count))

if __name__ == '__main__':
    main()
