import rsa
import stdio
import sys


# Entry point.
def main():
    # create lo and hi as int
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # get the public ke or private key as a tuple
    # which mean we are calling the function keygen
    keys = rsa.keygen(lo, hi)
    stdio.writeln(str(keys[0]) + " " + str(keys[1]) + " " + str(keys[2]))

if __name__ == "__main__":
    main()
