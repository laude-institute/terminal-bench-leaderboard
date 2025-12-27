def main():
    cowphabet = input().strip()
    heard = input().strip()
    order = {ch: i for i, ch in enumerate(cowphabet)}
    count = 1
    prev = -1
    for c in heard:
        idx = order[c]
        if idx <= prev:
            count += 1
        prev = idx
    print(count)

if __name__ == "__main__":
    main()
