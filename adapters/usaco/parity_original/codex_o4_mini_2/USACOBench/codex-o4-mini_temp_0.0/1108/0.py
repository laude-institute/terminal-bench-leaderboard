#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    cows = set()
    comfortable = set()

    # directions: up, down, left, right
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    def count_neighbors(x, y):
        return sum((x+dx, y+dy) in cows for dx, dy in dirs)

    def update_cell(x, y):
        # only update if cell has a cow
        if (x, y) not in cows:
            return
        cnt = count_neighbors(x, y)
        if cnt == 3:
            comfortable.add((x, y))
        else:
            comfortable.discard((x, y))

    for _ in range(n):
        x, y = map(int, input().split())
        cows.add((x, y))
        # update this cow and neighbors
        update_cell(x, y)
        for dx, dy in dirs:
            update_cell(x+dx, y+dy)
        # output current comfortable count
        print(len(comfortable))

if __name__ == '__main__':
    main()
