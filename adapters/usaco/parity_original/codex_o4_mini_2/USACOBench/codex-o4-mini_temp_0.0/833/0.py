#!/usr/bin/env python3
"""
1. Restate Problem:
   Given maternal relationships among cows, determine how two specific cows
   are related: siblings, direct ancestor (mother, grand-mother, etc.), aunt
   (aunt, great-aunt, etc.), cousins, or not related.

2. Conceptualization:
   - Build mapping: child -> mother, and reverse: mother -> list of children.
   - Generate ancestor lists for each cow by following mother pointers upward.
   - Check relationships in order:
     1. Siblings: same mother.
     2. Direct ancestor: one cow appears in the other's ancestry.
     3. Aunt: one cow is a non-direct child of an ancestor of the other.
     4. Cousins: share any common ancestor.
     5. Not related: none of the above.

3. Pseudocode:
   read N, cow1, cow2
   for each of N lines:
       read mom, child
       record mother[child] = mom
       append child to children[mom]
   define get_ancestry(cow):
       ancestors = []
       while cow has a mother:
           cow = mother[cow]
           ancestors.append(cow)
       return ancestors
   anc1 = get_ancestry(cow1)
   anc2 = get_ancestry(cow2)
   if cow1 and cow2 have same mother:
       print("SIBLINGS") and exit
   if cow2 in anc1:
       compute depth k and print ancestor relation
   if cow1 in anc2:
       compute depth k and print ancestor relation
   for each ancestor at depth k in anc1 (k>=2):
       if cow2 is a child of that ancestor but not on direct path:
           print aunt relation and exit
   repeat for anc2 (reversed roles)
   if anc1 and anc2 share any ancestor:
       print("COUSINS")
   else:
       print("NOT RELATED")
"""

import sys

def main():
    input_line = sys.stdin.readline().split()
    N = int(input_line[0])
    cow1, cow2 = input_line[1], input_line[2]

    mother = {}
    from collections import defaultdict
    children = defaultdict(list)

    for _ in range(N):
        mom, child = sys.stdin.readline().split()
        mother[child] = mom
        children[mom].append(child)

    def get_ancestry(cow):
        anc = []
        while cow in mother:
            cow = mother[cow]
            anc.append(cow)
        return anc

    anc1 = get_ancestry(cow1)
    anc2 = get_ancestry(cow2)

    # 1. Siblings
    if cow1 in mother and cow2 in mother and mother[cow1] == mother[cow2]:
        print("SIBLINGS")
        return

    # 2. Direct ancestor
    if cow2 in anc1:
        k = anc1.index(cow2) + 1
        if k == 1:
            relation = 'mother'
        elif k == 2:
            relation = 'grand-mother'
        else:
            relation = 'great-' * (k-2) + 'grand-mother'
        print(f"{cow2} is the {relation} of {cow1}")
        return
    if cow1 in anc2:
        k = anc2.index(cow1) + 1
        if k == 1:
            relation = 'mother'
        elif k == 2:
            relation = 'grand-mother'
        else:
            relation = 'great-' * (k-2) + 'grand-mother'
        print(f"{cow1} is the {relation} of {cow2}")
        return

    # 3. Aunt relations
    # cow2 relative to cow1
    for i, ancestor in enumerate(anc1):
        # i=0 is mother (k=1), need k>=2 for aunt
        if i == 0:
            continue
        parent = anc1[i-1]
        for child in children.get(ancestor, []):
            if child != parent and child == cow2:
                # prefix count = i-1 (i=1 -> aunt)
                prefix = i-1
                relation = 'great-' * prefix + 'aunt'
                print(f"{cow2} is the {relation} of {cow1}")
                return
    # cow1 relative to cow2
    for i, ancestor in enumerate(anc2):
        if i == 0:
            continue
        parent = anc2[i-1]
        for child in children.get(ancestor, []):
            if child != parent and child == cow1:
                prefix = i-1
                relation = 'great-' * prefix + 'aunt'
                print(f"{cow1} is the {relation} of {cow2}")
                return

    # 4. Cousins
    if set(anc1) & set(anc2):
        print("COUSINS")
    else:
        # 5. Not related
        print("NOT RELATED")

if __name__ == "__main__":
    main()
