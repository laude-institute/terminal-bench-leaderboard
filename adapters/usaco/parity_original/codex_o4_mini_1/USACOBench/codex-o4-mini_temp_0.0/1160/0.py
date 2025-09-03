#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    countA = [0] * (M+1)
    countB = [0] * (M+1)
    for _ in range(N):
        a = int(next(it))
        b = int(next(it))
        countA[a] += 1
        countB[b] += 1
    size = 2 * M
    # Compute convolution for starts
    C_AA = [0] * (size+1)
    for i in range(M+1):
        ci = countA[i]
        if ci == 0:
            continue
        # j >= i to avoid double counting
        for j in range(i, M+1):
            cj = countA[j]
            if cj == 0:
                continue
            s = i + j
            if i == j:
                C_AA[s] += ci * ci
            else:
                C_AA[s] += 2 * ci * cj
    # Compute convolution for ends
    C_BB = [0] * (size+1)
    for i in range(M+1):
        ci = countB[i]
        if ci == 0:
            continue
        for j in range(i, M+1):
            cj = countB[j]
            if cj == 0:
                continue
            s = i + j
            if i == j:
                C_BB[s] += ci * ci
            else:
                C_BB[s] += 2 * ci * cj
    # Prefix sums
    prefixA = [0] * (size+1)
    prefixB = [0] * (size+1)
    totalA = 0
    totalB = 0
    for k in range(size+1):
        totalA += C_AA[k]
        totalB += C_BB[k]
        prefixA[k] = totalA
        prefixB[k] = totalB
    # Output results for k = 0..2M
    out = []
    for k in range(size+1):
        less_end = prefixB[k-1] if k > 0 else 0
        ans = prefixA[k] - less_end
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
