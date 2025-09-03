#!/usr/bin/env python3
import sys

def main():
    # Read initial bucket sizes for both barns
    barn1 = list(map(int, sys.stdin.readline().split()))
    barn2 = list(map(int, sys.stdin.readline().split()))
    results = set()
    # Simulate all sequences of four moves (Tue, Wed, Thu, Fri)
    for i in range(len(barn1)):
        v1 = barn1[i]
        b1_1 = barn1[:i] + barn1[i+1:]
        b2_1 = barn2 + [v1]
        milk1_1 = 1000 - v1
        for j in range(len(b2_1)):
            v2 = b2_1[j]
            b2_2 = b2_1[:j] + b2_1[j+1:]
            b1_2 = b1_1 + [v2]
            milk1_2 = milk1_1 + v2
            for k in range(len(b1_2)):
                v3 = b1_2[k]
                b1_3 = b1_2[:k] + b1_2[k+1:]
                b2_3 = b2_2 + [v3]
                milk1_3 = milk1_2 - v3
                for l in range(len(b2_3)):
                    v4 = b2_3[l]
                    # Final transfer back to barn1
                    final_milk1 = milk1_3 + v4
                    results.add(final_milk1)
    # Output the number of distinct possible amounts in barn1
    print(len(results))

if __name__ == '__main__':
    main()
