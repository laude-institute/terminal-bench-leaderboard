import sys

def main():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    weights = list(map(int, input_data[1:]))
    # Convert weights to digit arrays (least significant first)
    digit_lists = []
    max_len = 0
    for w in weights:
        digits = []
        while w > 0:
            digits.append(w % 10)
            w //= 10
        digit_lists.append(digits)
        max_len = max(max_len, len(digits))

    best = 0

    # current sum of digits
    curr_sum = [0] * max_len

    def dfs(idx, count):
        nonlocal best, curr_sum
        if count > best:
            best = count
        # try adding more cows
        for i in range(idx, n):
            digits = digit_lists[i]
            ok = True
            # check for carry
            for j in range(len(digits)):
                if curr_sum[j] + digits[j] >= 10:
                    ok = False
                    break
            if not ok:
                continue
            # add digits
            for j in range(len(digits)):
                curr_sum[j] += digits[j]
            dfs(i + 1, count + 1)
            # backtrack
            for j in range(len(digits)):
                curr_sum[j] -= digits[j]

    dfs(0, 0)
    print(best)

if __name__ == "__main__":
    main()
