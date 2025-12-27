#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(10**7)
    from bisect import bisect_left
    input = sys.stdin.readline
    N,K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    # DSU with segment info
    parent = list(range(N))
    seg_l = list(range(N))
    seg_r = list(range(N))
    seg_size = [1]*N
    # Treap implementation
    import random
    class Node:
        __slots__ = ('key','prio','left','right')
        def __init__(self, key):
            self.key = key
            self.prio = random.random()
            self.left = None
            self.right = None

    def update(_): pass

    def split(root, key):
        if not root: return (None, None)
        if key <= root.key:
            L, R = split(root.left, key)
            root.left = R
            return (L, root)
        else:
            L, R = split(root.right, key)
            root.right = L
            return (root, R)

    def merge(a, b):
        if not a or not b: return a or b
        if a.prio < b.prio:
            a.right = merge(a.right, b)
            return a
        else:
            b.left = merge(a, b.left)
            return b

    def insert(root, node):
        if not root: return node
        if node.prio < root.prio:
            L, R = split(root, node.key)
            node.left, node.right = L, R
            return node
        elif node.key < root.key:
            root.left = insert(root.left, node)
        else:
            root.right = insert(root.right, node)
        return root

    def find_pred(root, key):
        # max node.key < key
        res = None
        while root:
            if root.key < key:
                res = root.key
                root = root.right
            else:
                root = root.left
        return res

    def find_succ(root, key):
        # min node.key > key
        res = None
        while root:
            if root.key > key:
                res = root.key
                root = root.left
            else:
                root = root.right
        return res

    # treap roots
    treap = [None]*N
    for i in range(N):
        treap[i] = Node(h[i])

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # neighbor pointers for segments
    left_nb = [i-1 for i in range(N)]
    right_nb = [i+1 for i in range(N)]
    right_nb[N-1] = -1

    # priority queue of candidate merges: (diff, left_l, right_l)
    import heapq
    pq = []
    for i in range(N-1):
        heapq.heappush(pq, (abs(h[i]-h[i+1]), i, i+1))

    # get minimal diff between segments a and b (roots)
    def get_min_diff(a, b):
        # traverse smaller treap
        # ensure a is smaller
        size_a = seg_size[a]
        size_b = seg_size[b]
        if size_a > size_b:
            a, b = b, a
        # in-order traverse a
        stack = []
        node = treap[a]
        mind = 10**18
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                x = node.key
                # pred
                p = find_pred(treap[b], x)
                if p is not None:
                    d = x-p if x>p else p-x
                    if d < mind: mind = d
                # succ
                s = find_succ(treap[b], x)
                if s is not None:
                    d = x-s if x>s else s-x
                    if d < mind: mind = d
                node = node.right
        return mind

    # merge treaps: small into large
    def merge_treap(a, b):  # returns root of merged
        # a small, b large
        # insert all from a into b
        stack = []
        node = treap[a]
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                # insert key
                nd = Node(node.key)
                treap[b] = insert(treap[b], nd)
                node = node.right
        return treap[b]

    # process merges
    while pq:
        diff, xi, yi = heapq.heappop(pq)
        if diff > K: break
        pi = find(xi)
        pj = find(yi)
        if pi == pj: continue
        # order by segment l
        if seg_l[pi] < seg_l[pj]:
            L, R = pi, pj
        else:
            L, R = pj, pi
        # must be adjacent segments
        if seg_r[L] + 1 != seg_l[R]: continue
        # recompute actual diff
        act = get_min_diff(L, R)
        if act > K: continue
        if act > diff:
            heapq.heappush(pq, (act, seg_l[L], seg_l[R]))
            continue
        # merge segments L and R
        # choose by size for treap merge
        if seg_size[L] < seg_size[R]:
            small, large = L, R
        else:
            small, large = R, L
        # merge small into large
        treap[large] = merge_treap(small, large)
        seg_size[large] += seg_size[small]
        # update segment bounds
        seg_l[large] = min(seg_l[L], seg_l[R])
        seg_r[large] = max(seg_r[L], seg_r[R])
        # DSU
        parent[small] = large
        # update neighbors
        left0 = left_nb[L]
        right0 = right_nb[R]
        if left0 != -1:
            right_nb[left0] = large
        if right0 != -1:
            left_nb[right0] = large
        left_nb[large] = left0
        right_nb[large] = right0
        # enqueue new neighbor merges on both sides
        if left0 != -1:
            heapq.heappush(pq, (get_min_diff(left0, large), seg_l[left0], seg_l[large]))
        if right0 != -1:
            heapq.heappush(pq, (get_min_diff(large, right0), seg_l[large], seg_l[right0]))

    # build result
    res = [0]*N
    i = 0
    while i < N:
        pi = find(i)
        l0 = seg_l[pi]
        r0 = seg_r[pi]
        vals = h[l0:r0+1]
        vals.sort()
        for j, v in enumerate(vals):
            res[l0+j] = v
        i = r0 + 1
    # output
    out = sys.stdout
    for v in res:
        out.write(str(v)+'\n')

if __name__ == '__main__':
    main()
