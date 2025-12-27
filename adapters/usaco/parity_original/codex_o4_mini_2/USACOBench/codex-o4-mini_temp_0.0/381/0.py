import sys
import bisect

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    intervals = []
    idx = 1
    for _ in range(n):
        start = int(data[idx]); end = int(data[idx+1])
        idx += 2
        intervals.append((end, start))
    intervals.sort()
    recorders = []  # sorted list of end times for each recorder
    count = 0
    for end, start in intervals:
        # find recorder that frees last but before start
        i = bisect.bisect_right(recorders, start) - 1
        if i >= 0:
            # reuse this recorder
            recorders.pop(i)
            bisect.insort(recorders, end)
            count += 1
        elif len(recorders) < 2:
            # open new recorder
            bisect.insort(recorders, end)
            count += 1
    print(count)

if __name__ == '__main__':
    main()
