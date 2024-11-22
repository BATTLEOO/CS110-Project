import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_reverse(s))


# Returns the reverse of the string s.
def _reverse(s):
    # use s[:-1]
    n = len(s)
    if n == 0:
        return s
    # s[n - 1] is the last element in the list, s[:n - 1]
    return s[n - 1] + _reverse(s[:n - 1])


if __name__ == "__main__":
    main()
