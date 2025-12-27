#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    B, E = map(int, input().split())
    # Read Bessie's moves
    b_moves = []
    total_b = 0
    for _ in range(B):
        dist, dirc = input().split()
        d = int(dist)
        total_b += d
        # direction: left = -1, right = +1
        b_moves.append((d, -1 if dirc == 'L' else 1))
    # Read Elsie's moves
    e_moves = []
    total_e = 0
    for _ in range(E):
        dist, dirc = input().split()
        d = int(dist)
        total_e += d
        e_moves.append((d, -1 if dirc == 'L' else 1))

    # Simulation parameters
    total_time = max(total_b, total_e)
    b_idx = e_idx = 0
    b_time = b_moves[0][0] if b_moves else 0
    e_time = e_moves[0][0] if e_moves else 0
    b_dir = b_moves[0][1] if b_moves else 0
    e_dir = e_moves[0][1] if e_moves else 0
    b_pos = e_pos = 0
    prev_equal = True  # start together, don't count initial
    meets = 0

    for _ in range(1, total_time + 1):
        # move Bessie
        if b_time > 0:
            b_pos += b_dir
            b_time -= 1
            if b_time == 0 and b_idx + 1 < len(b_moves):
                b_idx += 1
                b_time, b_dir = b_moves[b_idx]
        # move Elsie
        if e_time > 0:
            e_pos += e_dir
            e_time -= 1
            if e_time == 0 and e_idx + 1 < len(e_moves):
                e_idx += 1
                e_time, e_dir = e_moves[e_idx]

        # check meeting
        if b_pos == e_pos:
            if not prev_equal:
                meets += 1
            prev_equal = True
        else:
            prev_equal = False

    print(meets)

if __name__ == '__main__':
    main()
