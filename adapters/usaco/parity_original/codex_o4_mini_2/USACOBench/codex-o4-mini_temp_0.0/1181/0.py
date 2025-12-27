#!/usr/bin/env python3
import sys

def solve_case(h):
    n = len(h)
    # Single cow -> already equal
    if n == 1:
        return 0
    # Differences
    d = [h[i+1] - h[i] for i in range(n-1)]
    # Prefix sums for even-position operations x2, x4, ...
    m_even = (n-1) // 2
    ps_even = []
    for k in range(m_even):
        val = d[2*k] + (ps_even[k-1] if k > 0 else 0)
        ps_even.append(val)
        if val < 0:
            return -1
    # Offset sums for odd-position operations x1, x3, ...
    m_odd = n // 2
    offset_odd = [0] * m_odd
    for k in range(1, m_odd):
        offset_odd[k] = offset_odd[k-1] + d[2*k-1]
    # Determine final common level c
    if n % 2 == 0:
        # Even n: must satisfy endpoint consistency
        if h[0] + offset_odd[-1] != h[-1]:
            return -1
        # Maximize c under odd-position nonnegativity
        c_max = min(h[0] + off for off in offset_odd)
        c = c_max
        if c < 0:
            return -1
    else:
        # Odd n: c from last cow
        used_even = ps_even[-1] if ps_even else 0
        c = h[-1] - used_even
        # Check upper bound
        c_max = min(h[0] + off for off in offset_odd)
        if c < 0 or c > c_max:
            return -1
    # Compute total operations
    x1 = h[0] - c
    # Sum even ops
    total_ops = sum(ps_even)
    # Sum odd ops
    total_ops += x1 * m_odd + sum(offset_odd)
    # Bags = 2 * operations
    return total_ops * 2

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it))
        h = [int(next(it)) for _ in range(n)]
        out.append(str(solve_case(h)))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    main()
