#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    rects = []
    for i in range(N):
        x1,y1,x2,y2 = map(int, input().split())
        rects.append((x1, x2, y1, y2, i))
    # Sort by x1 ascending
    rects.sort(key=lambda r: (r[0], -r[1]))
    # Min-heap for active rectangles by x2
    import heapq
    heap = []  # elements: (x2, y1, y2, id)

    # Treap for y-intervals
    import random

    class Node:
        __slots__ = ('key', 'y2', 'prio', 'left', 'right', 'sub_max')
        def __init__(self, key, y2):
            self.key = key
            self.y2 = y2
            self.prio = random.random()
            self.left = None
            self.right = None
            self.sub_max = y2

    def update(n):
        n.sub_max = n.y2
        if n.left and n.left.sub_max > n.sub_max:
            n.sub_max = n.left.sub_max
        if n.right and n.right.sub_max > n.sub_max:
            n.sub_max = n.right.sub_max
        return n

    def rotate_right(y):
        x = y.left
        y.left = x.right
        x.right = y
        update(y)
        update(x)
        return x

    def rotate_left(x):
        y = x.right
        x.right = y.left
        y.left = x
        update(x)
        update(y)
        return y

    def treap_insert(root, node):
        if root is None:
            return node
        if node.key < root.key:
            root.left = treap_insert(root.left, node)
            if root.left.prio < root.prio:
                root = rotate_right(root)
        else:
            root.right = treap_insert(root.right, node)
            if root.right.prio < root.prio:
                root = rotate_left(root)
        return update(root)

    def treap_delete(root, key):
        if root is None:
            return None
        if key == root.key:
            # remove this node
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # both children exist, rotate to remove
            if root.left.prio < root.right.prio:
                root = rotate_right(root)
                root.right = treap_delete(root.right, key)
            else:
                root = rotate_left(root)
                root.left = treap_delete(root.left, key)
        elif key < root.key:
            root.left = treap_delete(root.left, key)
        else:
            root.right = treap_delete(root.right, key)
        if root:
            return update(root)
        return None

    def query_max_y2(root, key):
        # max y2 among keys <= key
        best = -1
        node = root
        while node:
            if node.key <= key:
                # candidate: node.y2 and left subtree
                if node.left and node.left.sub_max > best:
                    best = node.left.sub_max
                if node.y2 > best:
                    best = node.y2
                node = node.right
            else:
                node = node.left
        return best

    root = None
    count = 0
    for x1, x2, y1, y2, idx in rects:
        # remove expired
        while heap and heap[0][0] < x1:
            _, ry1, ry2, rid = heapq.heappop(heap)
            root = treap_delete(root, (ry1, rid))
        # check containment
        max_y2 = query_max_y2(root, (y1, N+1))
        if max_y2 < y2:
            count += 1
        # insert current
        heapq.heappush(heap, (x2, y1, y2, idx))
        node = Node((y1, idx), y2)
        root = treap_insert(root, node)
    print(count)

if __name__ == '__main__':
    main()
