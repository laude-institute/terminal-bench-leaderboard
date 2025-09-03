#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    cow1 = next(it)
    cow2 = next(it)
    mother = {}
    for _ in range(n):
        mom = next(it)
        child = next(it)
        mother[child] = mom

    def get_ancestors(cow):
        anc = {}
        depth = 1
        cur = mother.get(cow)
        while cur:
            anc[cur] = depth
            depth += 1
            cur = mother.get(cur)
        return anc

    anc1 = get_ancestors(cow1)
    anc2 = get_ancestors(cow2)

    # Siblings
    if mother.get(cow1) and mother.get(cow1) == mother.get(cow2):
        print("SIBLINGS")
        return

    # Direct ancestor relations
    def relation_name(prefix, base, d):  # prefix is 'great-' count, base is 'grand-mother' or 'aunt'
        if d == 1:
            return 'mother' if base == 'grand-mother' else base
        if base == 'grand-mother':
            if d == 2:
                return 'grand-mother'
            return 'great-' * (d - 2) + 'grand-mother'
        else:
            if d == 2:
                return 'aunt'
            return 'great-' * (d - 2) + 'aunt'

    # Check if cow2 is ancestor of cow1
    if cow2 in anc1:
        d = anc1[cow2]
        rel = relation_name('', 'grand-mother', d)
        print(f"{cow2} is the {rel} of {cow1}")
        return

    # Check if cow1 is ancestor of cow2
    if cow1 in anc2:
        d = anc2[cow1]
        rel = relation_name('', 'grand-mother', d)
        print(f"{cow1} is the {rel} of {cow2}")
        return

    # Check aunt relations
    m2 = mother.get(cow2)
    if m2 in anc1:
        d = anc1[m2]
        rel = relation_name('', 'aunt', d)
        print(f"{cow2} is the {rel} of {cow1}")
        return
    m1 = mother.get(cow1)
    if m1 in anc2:
        d = anc2[m1]
        rel = relation_name('', 'aunt', d)
        print(f"{cow1} is the {rel} of {cow2}")
        return

    # Cousins or not related
    if set(anc1.keys()) & set(anc2.keys()):
        print("COUSINS")
    else:
        print("NOT RELATED")

if __name__ == '__main__':
    main()
