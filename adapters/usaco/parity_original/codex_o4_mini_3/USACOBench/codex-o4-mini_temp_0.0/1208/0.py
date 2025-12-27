#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    input = sys.stdin.readline
    T = int(input())
    out = []
    for _ in range(T):
        M,N,K = map(int,input().split())
        f = list(map(int,input().split()))
        # build queues of positions for each folder
        from collections import deque
        qs = [deque() for _ in range(M+1)]
        for i,fi in enumerate(f, start=1): qs[fi].append(i)
        # BIT for dynamic list
        class BIT:
            def __init__(self,n):
                self.n = n; self.f = [0]*(n+1)
            def add(self,i,v):
                while i<=self.n:
                    self.f[i]+=v; i+=i&-i
            def sum(self,i):
                s=0
                while i>0:
                    s+=self.f[i]; i-=i&-i
                return s
            def find_kth(self,k):  # first idx where sum>=k
                idx=0; bitmask=1<<17
                while bitmask:
                    t = idx+bitmask
                    if t<=self.n and self.f[t]<k:
                        idx=t; k-=self.f[t]
                    bitmask>>=1
                return idx+1
        bit = BIT(N)
        for i in range(1,N+1): bit.add(i,1)
        import heapq
        LF = 1
        # prepare heap of (pos, folder)
        heap = []
        for folder in range(1, min(M,LF+K-1)+1):
            if qs[folder]: heapq.heappush(heap, (qs[folder][0], folder))
        total = N
        lowRank = 1
        ok = True
        for _ in range(N):
            # find next fileable
            while True:
                # candidate
                while heap:
                    pos,folder = heap[0]
                    if folder < LF or folder > LF+K-1 or not qs[folder] or qs[folder][0]!=pos:
                        heapq.heappop(heap); continue
                    break
                if heap:
                    pos,folder = heap[0]
                    # compute window
                    high = lowRank+K-1
                    if high>total: low = max(1, total-K+1); high = total
                    else: low = lowRank
                    rnk = bit.sum(pos)
                    if low <= rnk <= high:
                        # file it
                        heapq.heappop(heap)
                        qs[folder].popleft()
                        bit.add(pos, -1)
                        total -=1
                        # adjust lowRank if in last-K view
                        if low>1 and high==total+1:
                            lowRank = max(1, total-K+1)
                        # push next from this folder
                        if qs[folder] and LF <= folder <= LF+K-1:
                            heapq.heappush(heap, (qs[folder][0], folder))
                        break
                # no candidate or not in view: try scroll
                # scroll folder
                if LF+K-1 < M:
                    LF +=1
                    fnew = LF+K-1
                    if qs[fnew]: heapq.heappush(heap, (qs[fnew][0], fnew))
                    continue
                # scroll emails
                high = lowRank+K-1
                if high>total: low = max(1, total-K+1); high = total
                else: low = lowRank
                if high < total:
                    lowRank +=1; continue
                # cannot scroll any
                ok = False; break
            if not ok: break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
