import rsa
import stdio
import sys

# Entry point.
def main():
    # Public keys: accept n and e as int arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # get the number of bits for per character needed for encryption
    width = rsa.bitLength(n)

    # get the message from standard input, need to use stdio.readALL to read all the standard input, need to including \n
    message = stdio.readAll()

    # create a for loop, go through the message
    for c in message:

        # use function ord() to turn c into an integer x
        x = ord(c)

        # encrypt x one by one
        encrypted = rsa.encrypt(x, n, e)

        # we write the encrypted value as a width-long binary string, call rsa.dec2bin function, set encrypted width length and write in binary num in standard output
        stdio.write(rsa.dec2bin(encrypted, width))

    # write newline
    stdio.writeln()



if __name__ == "__main__":
    main()
