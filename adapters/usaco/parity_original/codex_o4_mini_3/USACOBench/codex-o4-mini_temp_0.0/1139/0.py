#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
def main():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    n = int(next(it))
    pts = [(0,0)] * n
    for i in range(n): pts[i] = (int(next(it)), int(next(it)))
    # Precompute segment intersections
    def orient(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    def on_seg(a, b, c):
        # check c on segment ab
        return min(a[0],b[0]) <= c[0] <= max(a[0],b[0]) and min(a[1],b[1]) <= c[1] <= max(a[1],b[1])
    def seg_int(i,j,k,l):
        a,b,c,d = pts[i], pts[j], pts[k], pts[l]
        o1 = orient(a,b,c)
        o2 = orient(a,b,d)
        o3 = orient(c,d,a)
        o4 = orient(c,d,b)
        if o1==0 and on_seg(a,b,c): return True
        if o2==0 and on_seg(a,b,d): return True
        if o3==0 and on_seg(c,d,a): return True
        if o4==0 and on_seg(c,d,b): return True
        return o1>0 and o2<0 or o1<0 and o2>0 and (o3>0 and o4<0 or o3<0 and o4>0)
    # store crosses in dict for pairs
    cross = {}
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                for l in range(k+1,n):
                    if len({i,j,k,l})<4: continue
                    cross[(i,j,k,l)] = seg_int(i,j,k,l)
    MOD = 10**9+7
    # DFS
    used = [False]*n
    segs = []  # list of (i,j)
    res = 0
    perm = []
    def dfs():
        nonlocal res
        k = len(perm)
        if k == n:
            res = (res+1) % MOD
            return
        for i in range(n):
            if used[i]: continue
            if k < 3:
                # always can add first 3
                new_neighbors = []
            else:
                # find visible previous neighbors
                vis = []
                ok = True
                for j in perm:
                    # check if segment i-j crosses any existing seg
                    cross_count = False
                    for u,v in segs:
                        a,b = min(i,j), max(i,j)
                        c,d = min(u,v), max(u,v)
                        if cross.get((a,b,c,d), False):
                            cross_count = True
                            break
                    if not cross_count:
                        vis.append(j)
                if len(vis) != 3:
                    continue
                new_neighbors = vis
            # choose i
            used[i] = True
            perm.append(i)
            # add segments
            added = []
            if k < 2:
                # p2: add segment to p1
                a,b = perm[-2], perm[-1]
                segs.append((a,b))
                added.append((a,b))
            elif k == 2:
                # p3: add triangle edges
                a,b,c = perm[0],perm[1],perm[2]
                for u,v in [(a,b),(b,c),(c,a)]:
                    segs.append((u,v))
                    added.append((u,v))
            else:
                # add for each vis neighbor
                for j in new_neighbors:
                    segs.append((i,j))
                    added.append((i,j))
            dfs()
            # backtrack
            for _ in added: segs.pop()
            perm.pop()
            used[i] = False
    dfs()
    print(res)

if __name__ == '__main__':
    main()
