import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    n = len(s)
    if n == 0:
        return True
    # use s[1:-1]
    if s[:1] == s[n - 1]:

        # return _isPalindrome(s[1:-1]). when touch the base case _isPalindrome return True
        return _isPalindrome(s[1:-1])

    # as long as not touching the else statement the function will always be True, when not equal, return false
    else:
        return False


if __name__ == "__main__":
    main()
