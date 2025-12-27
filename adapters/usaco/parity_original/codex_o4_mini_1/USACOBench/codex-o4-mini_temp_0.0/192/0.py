#!/usr/bin/env python3
import sys

def main():
    MOD = 2012
    s = sys.stdin.readline().strip()
    dp = {(0,0): 1}
    for c in s:
        new_dp = {}
        for (h, g), val in dp.items():
            # assign to H
            nh = h + (1 if c == '(' else -1)
            if nh >= 0:
                new_dp[(nh, g)] = (new_dp.get((nh, g), 0) + val) % MOD
            # assign to G
            ng = g + (1 if c == '(' else -1)
            if ng >= 0:
                new_dp[(h, ng)] = (new_dp.get((h, ng), 0) + val) % MOD
        dp = new_dp
    print(dp.get((0, 0), 0))

if __name__ == "__main__":
    main()
