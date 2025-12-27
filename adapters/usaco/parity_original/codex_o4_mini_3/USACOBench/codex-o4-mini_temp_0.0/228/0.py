#!/usr/bin/env python3
"""
Party Invitations

Farmer John invites cows with group constraints:
if k-1 cows in a group of size k are invited, the last must be invited.
Starting with cow 1 invited, compute minimal invited cows.
"""
import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    N, G = map(int, input().split())
    # Store group data
    group_size = [0] * G
    group_members = [None] * G
    invited_counts = [0] * G
    cow_groups = defaultdict(list)
    for i in range(G):
        parts = list(map(int, input().split()))
        S, members = parts[0], parts[1:]
        group_size[i] = S
        group_members[i] = members
        for c in members:
            cow_groups[c].append(i)

    invited = [False] * (N + 1)
    # Start by inviting cow 1
    invited[1] = True
    # Initialize counts for groups containing cow 1
    for g in cow_groups.get(1, []):
        invited_counts[g] += 1

    # Queue groups ready to trigger (one missing cow)
    queue = deque()
    for i in range(G):
        if group_size[i] - invited_counts[i] == 1:
            queue.append(i)

    # Process constraints
    while queue:
        g = queue.popleft()
        # Re-check in case counts changed
        if group_size[g] - invited_counts[g] != 1:
            continue
        # Invite the missing cow in this group
        for c in group_members[g]:
            if not invited[c]:
                invited[c] = True
                # Update all groups of this newly invited cow
                for h in cow_groups.get(c, []):
                    invited_counts[h] += 1
                    if group_size[h] - invited_counts[h] == 1:
                        queue.append(h)
                break

    # Output result: total invited cows
    print(sum(invited))

if __name__ == '__main__':
    main()
