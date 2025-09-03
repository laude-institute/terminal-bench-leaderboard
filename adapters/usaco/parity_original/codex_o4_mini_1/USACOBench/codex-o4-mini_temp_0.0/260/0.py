#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    N, K = map(int, data)
    last = {}
    ans = -1
    for i in range(N):
        line = sys.stdin.readline()
        if not line:
            break
        b = int(line)
        if b in last and i - last[b] <= K:
            ans = b if b > ans else ans
        last[b] = i
    print(ans)

if __name__ == "__main__":
    main()
