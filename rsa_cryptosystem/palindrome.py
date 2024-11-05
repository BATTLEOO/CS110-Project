import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    for j in range(len(s)//2):
        if s[j] == s[len(s) - j - 1]:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
