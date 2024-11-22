from http.cookiejar import uppercase_escaped_char

import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))


# Returns True if pwd is a valid password, and False otherwise.
def _isValid(pwd):
    # set check1, check2, check3, check4, check5 to False
    check1, check2, check3, check4, check5 = False, False, False, False, False
    if len(pwd) == 8:
        check1 = True
    for c in pwd:
        if c.isdigit():
            check2 = True
        elif c.isupper():
            check3 = True
        elif c.islower():
            check4 = True
        elif not c.isalpha():
            check5 = True
    return check1 and check2 and check3 and check4 and check5




if __name__ == "__main__":
    main()
