#!/usr/bin/env python3

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    B = list(map(int, data[1:1+n]))
    # initial max block without removal
    ans = 0
    prev = None
    cnt = 0
    for b in B:
        if b == prev:
            cnt += 1
        else:
            prev = b
            cnt = 1
        if cnt > ans:
            ans = cnt
    # consider removing each breed
    breeds = set(B)
    for rem in breeds:
        prev = None
        cnt = 0
        for b in B:
            if b == rem:
                continue
            if b == prev:
                cnt += 1
            else:
                prev = b
                cnt = 1
            if cnt > ans:
                ans = cnt
    print(ans)

if __name__ == '__main__':
    main()
