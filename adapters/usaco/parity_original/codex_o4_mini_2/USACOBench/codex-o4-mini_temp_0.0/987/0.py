#!/usr/bin/env python3

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0]); K = int(data[1])
    words = data[2:]
    current_len = 0
    first_word_in_line = True
    for w in words:
        if current_len + len(w) <= K:
            if not first_word_in_line:
                print(' ', end='')
            print(w, end='')
            current_len += len(w)
            first_word_in_line = False
        else:
            print()
            print(w, end='')
            current_len = len(w)
            first_word_in_line = False
    print()

if __name__ == '__main__':
    main()
