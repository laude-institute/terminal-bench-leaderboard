#!/usr/bin/env python3
"""
Reads a string of parentheses and counts the number of ways
to find a '(( ' substring before a '))' substring.
"""
def main():
    s = input().strip()
    count_left = 0
    result = 0
    # Traverse string, count '((' and for each '))' add previous '((' count
    for i in range(len(s) - 1):
        if s[i] == '(' and s[i+1] == '(':  # hind legs
            count_left += 1
        elif s[i] == ')' and s[i+1] == ')':  # front legs
            result += count_left
    print(result)

if __name__ == "__main__":
    main()
