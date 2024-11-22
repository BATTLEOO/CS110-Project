import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    n = int(sys.argv[1])
    stdio.writeln(_sumOfInts(n))


# Returns the sum 1 + 2 + ... + n.
def _sumOfInts(n):
    # set up base n == 1 , return 1
    if n == 1:
        return 1

    # write recursion if n > 1, return n + _sumOfInts(n - 1)
    elif n > 1:
        return n + _sumOfInts(n - 1)



if __name__ == "__main__":
    main()
