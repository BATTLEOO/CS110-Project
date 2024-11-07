import rsa
import stdio
import sys

# Entry point.
def main():
    # Public keys: accept n and e as command line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # get the number of bits for per character needed for encryption, here is bits of n as at least
    width = rsa.bitLength(n)

    # get the message from standard input
    # !!!! need to use reads all to read all the standard input
    # including the \n, which is
    message = stdio.readAll()

    # create a for loop, because we want to over the message
    for c in message:

        # use the build-in function ord() to turn c into an integer x
        x = ord(c)

        # now we encrypt our x
        encrypted = rsa.encrypt(x, n, e)

        # we change the encrypted value every loop

        # we write the encrypted value as a width-long binary string
        stdio.write(rsa.dec2bin(encrypted, width))
    stdio.writeln()



if __name__ == "__main__":
    main()

