import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    # set n to the number of characters in s
    n = len(s)

    # create for i in range 0 to n//2
    for i in range(n // 2 + 1):

        # check if the element is the same, write if not the same return false e.g for 0 compare len -1 （last element in the list）
        if s[i] != s[n - i - 1]:

            # if not same return False
            return False

    # return Ture when if statement do not return false
    return True

if __name__ == "__main__":
    main()
