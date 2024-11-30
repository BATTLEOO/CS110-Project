import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_reverse(s))


# Returns the reverse of the string s.
def _reverse(s):
    # set n to the length of s
    n = len(s)

    # Base case: if n = 0, return the empty string
    if n == 0:
        return s

    # s[n - 1] is the last element in the list, s[:n - 1]
    # Return a concatenation of s[n - 1] and _reverse(s[:n - 1])
    return s[n - 1] + _reverse(s[:n - 1])


if __name__ == "__main__":
    main()
