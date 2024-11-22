import stdio
import sys


# Entry point. [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writef("zeros = %d, ones = %d, total = %d\n", _zeros(s), _ones(s), len(s))


# Return the number of zeros in s.
def _zeros(s):
    # Base case: if s is empty, return 0
    if len(s) == 0:
        return 0

    # remember 0 is string need to use'', if not, the if statement will not check zero correctly
    if s[:1] == '0':

        # if zero return 1 + _zeros(s[1:])
        return 1 + _zeros(s[1:])

    # otherwise return _zeros(s[1:])
    else:
        return _zeros(s[1:])




# Return the number of ones in s.
def _ones(s):
    # Base case: if s is empty, return 0
    if len(s) == 0:
        return 0

    # remember 1 is string need to use'', if not, the if statement will not check one correctly
    if s[:1] == '1':

        # if 1, return 1 + _ones(s[1:])
        return 1 + _ones(s[1:])

    # otherwise return _ones(s[1:])
    else:
        return _ones(s[1:])


if __name__ == "__main__":
    main()
