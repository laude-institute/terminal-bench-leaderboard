#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    ptr = 1
    out_lines = []
    for _ in range(t):
        s = data[ptr]; ptr += 1
        tgt = data[ptr]; ptr += 1
        n = len(s)
        # Build direct mapping
        mapping = {}
        impossible = False
        for i in range(n):
            c = s[i]
            d = tgt[i]
            if c in mapping:
                if mapping[c] != d:
                    impossible = True
                    break
            else:
                mapping[c] = d
        if impossible:
            out_lines.append("-1")
            continue
        # Build graph of necessary transformations
        adj = {}
        nodes = set()
        for c, d in mapping.items():
            nodes.add(c)
            nodes.add(d)
            if c != d:
                adj.setdefault(c, []).append(d)
        # Count total edges
        m = sum(1 for c, d in mapping.items() if c != d)
        # Tarjan's algorithm for SCC
        index = {}
        lowlink = {}
        onstack = {}
        stack = []
        idx = 0
        scc_count = 0

        def strongconnect(v):
            nonlocal idx, scc_count
            index[v] = idx
            lowlink[v] = idx
            idx += 1
            stack.append(v)
            onstack[v] = True
            for w in adj.get(v, []):
                if w not in index:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif onstack.get(w, False):
                    lowlink[v] = min(lowlink[v], index[w])
            # If v is root of SCC
            if lowlink[v] == index[v]:
                scc = []
                while True:
                    w = stack.pop()
                    onstack[w] = False
                    scc.append(w)
                    if w == v:
                        break
                if len(scc) > 1:
                    scc_count += 1

        # Run Tarjan on all nodes
        for v in nodes:
            if v not in index:
                strongconnect(v)
        # Answer is edges + number of cycles
        res = m + scc_count
        out_lines.append(str(res))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
