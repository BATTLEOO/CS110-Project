import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):

    # create for i in range len(s)/2
    for j in range(len(s)//2):

        # check the element is the same, e.g for 0 compare len -1 （last element in the list）
        if s[j] != s[len(s) - j - 1]:

            # if not same return False
            return False

    # return Ture no false happen in the if statement
    return True

if __name__ == "__main__":
    main()
