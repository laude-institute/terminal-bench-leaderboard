def main():
    # Read number of words N and max non-space chars K per line
    N, K = map(int, input().split())
    words = input().split()

    current_count = 0  # count of non-space characters on current line
    current_line = []  # words on current line

    for w in words:
        # Check if word fits on current line
        if current_count + len(w) <= K:
            current_line.append(w)
            current_count += len(w)
        else:
            # Print current line and start a new one
            print(" ".join(current_line))
            current_line = [w]
            current_count = len(w)

    # Print the last line if any words remain
    if current_line:
        print(" ".join(current_line))


if __name__ == "__main__":
    main()
