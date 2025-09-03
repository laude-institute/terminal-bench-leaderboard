#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    T = int(next(it))
    state_str = next(it).strip()
    final_state = [c == '1' for c in state_str]
    # read and sort interactions by time
    events = []
    for _ in range(T):
        t = int(next(it)); x = int(next(it)) - 1; y = int(next(it)) - 1
        events.append((t, x, y))
    events.sort(key=lambda x: x[0])

    valid_pairs = []  # list of (patient_zero, K)
    # simulate for each possible patient zero
    for p0 in range(N):
        # try K from 0 to T
        for K in range(T+1):
            infected = [False] * N
            passes = [0] * N
            infected[p0] = True
            for _, x, y in events:
                # x infects y
                if infected[x] and passes[x] < K:
                    if not infected[y]:
                        infected[y] = True
                    passes[x] += 1
                # y infects x
                if infected[y] and passes[y] < K:
                    if not infected[x]:
                        infected[x] = True
                    passes[y] += 1
            if infected == final_state:
                valid_pairs.append((p0, K))
    # gather results
    patient_zeros = set(p for p, k in valid_pairs)
    Ks = [k for p, k in valid_pairs]
    minK = min(Ks)
    maxK = max(Ks)
    # if maxK == T, then infinite is possible
    infinite = any(k == T for k in Ks)
    # output
    out = []
    out.append(str(len(patient_zeros)))
    out.append(str(minK))
    out.append('Infinity' if infinite else str(maxK))
    print(' '.join(out))

if __name__ == '__main__':
    main()
