#!/usr/bin/env python3

def min_keystrokes(a, b):
    mapping = {}
    for c1, c2 in zip(a, b):
        if c1 != c2:
            if c1 in mapping and mapping[c1] != c2:
                return -1
            mapping[c1] = c2
    edges = len(mapping)
    visited = set()
    cycles = 0
    for node in mapping:
        if node not in visited:
            cur = node
            path = set()
            while True:
                if cur not in mapping:
                    break
                if cur in path:
                    cycles += 1
                    break
                path.add(cur)
                cur = mapping[cur]
            visited |= path
    if cycles > 0:
        used = set(a) | set(b)
        spare_found = False
        for i in range(ord('a'), ord('z')+1):
            c = chr(i)
            if c not in used:
                spare_found = True
                break
        if not spare_found:
            for i in range(ord('A'), ord('Z')+1):
                c = chr(i)
                if c not in used:
                    spare_found = True
                    break
        if not spare_found:
            return -1
    return edges + cycles

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    res = []
    for _ in range(t):
        a = data[idx]; b = data[idx+1]
        idx += 2
        res.append(str(min_keystrokes(a, b)))
    print('\n'.join(res))

if __name__ == '__main__':
    main()
