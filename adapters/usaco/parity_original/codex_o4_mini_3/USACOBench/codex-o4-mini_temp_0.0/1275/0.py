#!/usr/bin/env python3
import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n+1)
    def add(self, i, v):
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    E = list(map(int, data[2:2+n]))

    # find last positions
    lastG = max(i+1 for i, c in enumerate(s) if c == 'G')
    lastH = max(i+1 for i, c in enumerate(s) if c == 'H')

    AG = []  # auto-cover G
    BG = {}  # G needing to cover h: pos -> E
    AH = []  # auto-cover H
    BH = {}  # H needing to cover g: pos -> E

    for i, c in enumerate(s, start=1):
        e = E[i-1]
        if c == 'G':
            if e >= lastG:
                AG.append(i)
            else:
                BG[i] = e
        else:
            if e >= lastH:
                AH.append(i)
            else:
                BH[i] = e

    # case 1
    ans = len(AG) * len(AH)

    # case 2: g auto, h in BH must cover g
    AG.sort()
    import bisect
    for h, eh in BH.items():
        cnt = bisect.bisect_right(AG, eh)
        ans += cnt

    # case 3: h auto, g in BG must cover h
    AH.sort()
    for g, eg in BG.items():
        cnt = bisect.bisect_right(AH, eg)
        ans += cnt

    # case 4: both need to cover each other
    # prepare removal events for H
    remove = [[] for _ in range(n+2)]
    for h, eh in BH.items():
        idx = eh + 1
        if idx <= n:
            remove[idx].append(h)

    fw = Fenwick(n)
    for h in BH:
        fw.add(h, 1)

    # sweep g from n down to 1
    for g in range(n, 0, -1):
        for h in remove[g]:
            fw.add(h, -1)
        if g in BG:
            eg = BG[g]
            if eg > 0:
                ans += fw.sum(eg)

    print(ans)

if __name__ == '__main__':
    main()
