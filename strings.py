# Ashton Johnson, CS 543, Assignment 1
#
# This program takes in a filename, encoding type (default to UTF-8), and threshold (default 4)
# It implements the unix command "strings"
# It prints out every string encoded with the given encoding that is equal to or longer than the given threshold

import argparse
import string


def main():
    # Adding arguments parsers for file, e, and n
    parser = argparse.ArgumentParser(description='Print the printable strings from a file.')
    parser.add_argument('filename')
    parser.add_argument('-n', metavar='min-len', type=int, default=4,
                        help='Print sequences of characters that are at least min-len characters long')
    parser.add_argument('-e', metavar='encoding', choices=('s', 'l', 'b'), default='s',
                        help='Select the character encoding of the strings that are to be found. ' +
                        'Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, ' +
                        'l = little endian UTF-16.')
    args = parser.parse_args()

    # Iterates over strings() and prints out each yielded string
    for s in strings(args.filename, args.n, args.e):
        print(s)


def strings(file, n, e):
    # Opens file in read binary mode
    with open(file, 'rb') as f:
        # Variable for storing result string
        result = ""
        # UTF-8
        if e == 's':
            # For each char in f
            for c in f.read().decode("utf-8", "ignore"):
                # Check if printable
                if c in string.printable:
                    # Add into result
                    result += c
                    # Allows looping until non-printable character
                    continue
                # Checks if result reaches n requirement
                if len(result) >= n:
                    yield result
                # Resets result
                result = ""
            if len(result) >= n:
                yield result
        # UTF-16 little endian
        elif e == 'l':
            for c in f.read().decode("utf-16-le", "ignore"):
                if c in string.printable:
                    result += c
                    continue
                if len(result) >= n:
                    yield result
                result = ""
            if len(result) >= n:
                yield result
        # UTF-16 big endian
        elif e == 'b':
            for c in f.read().decode("utf-16-be", "ignore"):
                if c in string.printable:
                    result += c
                    continue
                if len(result) >= n:
                    yield result
                result = ""
            if len(result) >= n:
                yield result


if __name__ == '__main__':
    main()
