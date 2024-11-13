import rsa
import stdio
import sys


# Entry point.
def main():
    # create lo and hi as int arguments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # call function rsa.keygen to get public/private keys as a tuple
    keys = rsa.keygen(lo, hi)

    # write in standard output, write the three values separated by a space
    stdio.writeln(str(keys[0]) + " " + str(keys[1]) + " " + str(keys[2]))

if __name__ == "__main__":
    main()
