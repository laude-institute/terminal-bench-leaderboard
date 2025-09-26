#!/usr/bin/env python3
import sys

def simulate(N, interactions, final_states, patient_zero, K):
    infected = [False] * N
    handshake_count = [0] * N
    infected[patient_zero] = True
    # process interactions in time order
    for _, x, y in interactions:
        pre_x = infected[x]
        pre_y = infected[y]
        # attempt infections based on contagious shakes left
        if pre_x and handshake_count[x] < K:
            infected[y] = True
        if pre_y and handshake_count[y] < K:
            infected[x] = True
        # count this handshake for infected cows
        if pre_x:
            handshake_count[x] += 1
        if pre_y:
            handshake_count[y] += 1
    # verify final infection states match observed
    for i in range(N):
        if infected[i] != (final_states[i] == 1):
            return False
    return True

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    T = int(next(it))
    state_str = next(it).strip()
    final_states = [int(c) for c in state_str]
    interactions = []
    for _ in range(T):
        t = int(next(it))
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        interactions.append((t, x, y))
    interactions.sort(key=lambda x: x[0])

    candidate_count = 0
    minK_overall = T + 1
    maxK_overall = -1
    infinite = False

    # test each cow as patient zero
    for cow in range(N):
        valid_Ks = []
        for K in range(0, T + 1):
            if simulate(N, interactions, final_states, cow, K):
                valid_Ks.append(K)
        if valid_Ks:
            candidate_count += 1
            kmin = min(valid_Ks)
            kmax = max(valid_Ks)
            if kmin < minK_overall:
                minK_overall = kmin
            # if K==T works, infinite possible
            if kmax == T:
                infinite = True
            else:
                if kmax > maxK_overall:
                    maxK_overall = kmax

    # prepare output
    if minK_overall == T + 1:
        minK_overall = 0
    # print results
    if infinite:
        print(candidate_count, minK_overall, "Infinity")
    else:
        print(candidate_count, minK_overall, maxK_overall)

if __name__ == '__main__':
    main()
