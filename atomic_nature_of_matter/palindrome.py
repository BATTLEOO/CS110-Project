import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    # set n to the length of s
    n = len(s)

    # Base case: if n = 0, return True
    if n == 0:
        return True

    # return True if the first character (s[:1]) in s is the same as the last character(s[n - 1])
    if s[:1] == s[n - 1]:

        # return _isPalindrome(s[1:-1]). When touch the base case _isPalindrome return True
        return _isPalindrome(s[1:-1])

    # else: as long as not touching the else statement the function will always be True, when not equal, return false
    else:
        return False


if __name__ == "__main__":
    main()
