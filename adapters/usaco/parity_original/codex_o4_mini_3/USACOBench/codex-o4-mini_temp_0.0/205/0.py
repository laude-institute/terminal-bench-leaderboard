#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    B = int(next(it)); E = int(next(it))
    B_moves = []
    for _ in range(B):
        d = int(next(it)); dir = next(it)
        v = 1 if dir == 'R' else -1
        B_moves.append([d, v])
    E_moves = []
    for _ in range(E):
        d = int(next(it)); dir = next(it)
        v = 1 if dir == 'R' else -1
        E_moves.append([d, v])
    # indices and remaining times
    i = j = 0
    rem_b = B_moves[0][0] if B_moves else float('inf')
    rem_e = E_moves[0][0] if E_moves else float('inf')
    v_b = B_moves[0][1] if B_moves else 0
    v_e = E_moves[0][1] if E_moves else 0
    pos_b = pos_e = 0
    time = 0
    together = True
    greetings = 0
    while i < len(B_moves) or j < len(E_moves):
        # determine dt
        if i < len(B_moves):
            rem_b = B_moves[i][0]
            v_b = B_moves[i][1]
        else:
            rem_b = float('inf'); v_b = 0
        if j < len(E_moves):
            rem_e = E_moves[j][0]
            v_e = E_moves[j][1]
        else:
            rem_e = float('inf'); v_e = 0
        dt = min(rem_b, rem_e)
        # check meeting in (0, dt]
        dx = pos_e - pos_b
        dv = v_b - v_e
        if dv != 0:
            num = dx
            den = dv
            # t_offset = num/den
            # want 0 < t_offset <= dt
            if num * den > 0 and abs(num) <= abs(den) * dt:
                # they meet
                if not together:
                    greetings += 1
                    together = True
        else:
            # same velocity
            if dx == 0 and dt > 0:
                if not together:
                    greetings += 1
                    together = True
        # advance time and positions
        pos_b += v_b * dt
        pos_e += v_e * dt
        time += dt
        # subtract dt from current segments
        if i < len(B_moves):
            B_moves[i][0] -= dt
            if B_moves[i][0] == 0:
                i += 1
        if j < len(E_moves):
            E_moves[j][0] -= dt
            if E_moves[j][0] == 0:
                j += 1
        # update together flag if now apart
        if pos_b != pos_e:
            together = False
    # output greetings
    sys.stdout.write(str(greetings))

if __name__ == '__main__':
    main()
