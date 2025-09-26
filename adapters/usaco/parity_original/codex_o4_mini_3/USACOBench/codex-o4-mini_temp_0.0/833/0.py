#!/usr/bin/env python3
"""
Genealogy relationship finder for cows.
"""
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    cow1, cow2 = data[1], data[2]
    pairs = data[3:]
    parent = {}
    # build parent map: child -> mother
    for i in range(0, len(pairs), 2):
        mom, child = pairs[i], pairs[i+1]
        parent[child] = mom

    def get_ancestors(cow):
        # returns list of ancestors: [mother, grandmother, ...]
        anc = []
        while cow in parent:
            cow = parent[cow]
            anc.append(cow)
        return anc

    anc1 = get_ancestors(cow1)
    anc2 = get_ancestors(cow2)

    # helper to build relation string for ancestor at depth d
    def ancestor_relation(depth):
        if depth == 1:
            return 'mother'
        if depth == 2:
            return 'grand-mother'
        # depth >=3: great-(depth-2)-grand-mother
        return 'great-' * (depth-2) + 'grand-mother'

    # helper to build relation string for aunt at depth d
    def aunt_relation(depth):
        # depth: ancestor depth of aunt's mother
        if depth == 2:
            return 'aunt'
        # depth >=3: great-(depth-2)-aunt
        return 'great-' * (depth-2) + 'aunt'

    # 1. siblings
    p1 = parent.get(cow1)
    p2 = parent.get(cow2)
    if p1 and p1 == p2:
        print('SIBLINGS')
        return

    # 2. direct ancestor
    if cow2 in anc1:
        d = anc1.index(cow2) + 1
        rel = ancestor_relation(d)
        print(f"{cow2} is the {rel} of {cow1}")
        return
    if cow1 in anc2:
        d = anc2.index(cow1) + 1
        rel = ancestor_relation(d)
        print(f"{cow1} is the {rel} of {cow2}")
        return

    # 3. aunt relationship
    # cow2 is aunt of cow1?
    m2 = parent.get(cow2)
    if m2 and m2 in anc1:
        d = anc1.index(m2) + 1
        if d >= 2:
            rel = aunt_relation(d)
            print(f"{cow2} is the {rel} of {cow1}")
            return
    # cow1 is aunt of cow2?
    m1 = parent.get(cow1)
    if m1 and m1 in anc2:
        d = anc2.index(m1) + 1
        if d >= 2:
            rel = aunt_relation(d)
            print(f"{cow1} is the {rel} of {cow2}")
            return

    # 4. cousins if share any common ancestor
    if set(anc1) & set(anc2):
        print('COUSINS')
    else:
        print('NOT RELATED')

if __name__ == '__main__':
    main()
