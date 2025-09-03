#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    # Read sprinklers: exactly one per row
    # P[row] = col
    P = [0]*n
    for _ in range(n):
        x = int(next(it)); y = int(next(it))
        P[x] = y
    # Build inverse: invP[col] = row
    invP = [0]*n
    for row, col in enumerate(P):
        invP[col] = row
    # Compute prefix min A[y] = min(invP[0..y])
    A = [0]*n
    cur = n
    for y in range(n):
        if invP[y] < cur:
            cur = invP[y]
        A[y] = cur
    # Compute suffix max B[y] = max(invP[y..n-1])
    B = [0]*n
    cur = -1
    for y in range(n-1, -1, -1):
        if invP[y] > cur:
            cur = invP[y]
        B[y] = cur
    MOD = 10**9+7
    # Prefix sums of B and B^2
    prefixB = [0]*n
    prefixB2 = [0]*n
    s1 = 0; s2 = 0
    for i in range(n):
        b = B[i]
        s1 = (s1 + b) % MOD
        s2 = (s2 + b*b) % MOD
        prefixB[i] = s1
        prefixB2[i] = s2
    inv2 = (MOD+1)//2
    ans = 0
    # For each y1 = i, y2 = j > i
    # L = A[i], R = B[j], require A[i] <= B[j]
    # Sum C(R-L+1,2) over j>i where B[j]>=A[i]
    # Precompute binary search on B (non-increasing)
    # B is non-increasing: B[0]>=B[1]>=...>=B[n-1]
    import bisect
    # Build array of (-B[j]) which is non-decreasing
    negB = [-b for b in B]
    # For each i
    for i in range(n-1):
        Ai = A[i]
        # find last j with B[j] >= Ai
        # i.e., first index in negB where -B[j] > -Ai, then minus one
        key = -Ai
        # bisect_right gives first pos where negB[pos] > key
        pos = bisect.bisect_right(negB, key)
        q = pos - 1
        # count j in [i+1..q]
        L = i+1
        R = q
        if R < L:
            continue
        cnt = R - L + 1
        sumB = prefixB[R] - (prefixB[L-1] if L>0 else 0)
        sumB %= MOD
        sumB2 = prefixB2[R] - (prefixB2[L-1] if L>0 else 0)
        sumB2 %= MOD
        # sum of C(B[j]-Ai+1,2) = sum[(B[j]^2 - (2*Ai-1)*B[j] + Ai*(Ai-1)) / 2]
        term1 = sumB2
        term2 = ( (2*Ai - 1) % MOD ) * sumB % MOD
        term3 = cnt * (Ai * (Ai - 1) % MOD) % MOD
        total = (term1 - term2 + term3) % MOD
        total = total * inv2 % MOD
        ans = (ans + total) % MOD
    print(ans)

if __name__ == "__main__":
    main()
