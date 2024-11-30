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

    # if length of pwd is at least 8, set check1 to True
    if len(pwd) == 8:
        check1 = True

    # for each character c in pwd
    for c in pwd:

        # If c is a digit, set check2 to True
        if c.isdigit():
            check2 = True

        # Else if c is upper case, set check3 to True
        elif c.isupper():
            check3 = True

        # Else if c is lower case, set check4 to True
        elif c.islower():
            check4 = True

        # Else if c is not alphanumeric, set check5 to True
        elif not c.isalpha():
            check5 = True

    # Return check1, check2, check3, check4, and check5 (boolean statement)
    return check1 and check2 and check3 and check4 and check5




if __name__ == "__main__":
    main()
