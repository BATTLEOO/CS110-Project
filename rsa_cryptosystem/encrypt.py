import rsa
import stdio
import sys

import rsa
import sys

# Entry point.






# Entry point.
def main():
    # Public keys: accept n and e as command line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # get the number of bits for per character needed for encryption, here is bits of n as at least
    width = rsa.bitLength(n)
    print(width)

    # get the message from standard input
    message = stdio.readString()

    encrypted_message = []

    # create a for loop, because we want to over the message
    for c in range(len(message)):

        # use the build-in function ord() to turn c into an integer x
        x = ord(message[c])

        # now we encrypt our x
        encrypted = rsa.encrypt(x, n, e)

        # we change the encrypted value every loop
        dec = rsa.dec2bin(encrypted, width)

        encrypted_message += [dec]
        # we write the encrypted value as a width-long binary string
        # print(dec, end='')
    stdio.writef("%s\n", " ".join(encrypted_message))
    stdio.writeln()

#
# if __name__ == "__main__":
#     main()

#000110000000 010011010100 001010100011 001010100011 001110000110 010111100100
#000110000000 010011010100 001010100011 001010100011 001110000110
# MY OUTPUT HAVE MISSING DATA
# IT MIGHT MISSING THE LAST ELEMENT IN IT.

# len = 5
# x 67
# en 384
# 000110000000
# 00011000000083
# 1236
# 010011010100
# 01001101010049
# 675
# 001010100011
# 00101010001149
# 675
# 001010100011
# 00101010001148
# 902
# 001110000110
# 001110000110