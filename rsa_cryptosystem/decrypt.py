import rsa
import stdio
import sys


# Entry point.
def main():
    # private key: accept n and d as int
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # get the number of bits per character(width)
    # this mean we have to get the numer of bits for every character
    # use bitLength, it returns the least number of bits needed to represents n
    width = rsa.bitLength(n)
    print(width)

    # use readString to read the input from standard input, which will be the data from the encrypt.py.
    message = stdio.readString()

    # set l as the length of message
    l = len(message)

    # create a for loop that is from  to l -1(exclude), and the step is width
    # one range of width is one character, and we convert the width to character
    # This is the idea of the covert from binary to character
    for i in range(0, l, width):

        # we set s as a part of the list from i to i + width
        # which is the number of message that we need, everytime we loop, we cut small piece of the data from message
        s = message[i : i + width]

        # after we get s, we convert the binary string s to decimal representation
        # here we use the bin2dec to convert binary to decimal
        y = rsa.bin2dec(s)

        # now we are ready to decrypt our y to character
        decrypted = rsa.decrypt(y, n, d)

        # we obtained the value by using the built-in function chr()
        stdio.write(chr(decrypted))
    stdio.writeln()

if __name__ == "__main__":
    main()
# for code running
# 000110000000010011010100001010100011001010100011001110000110010111100100
# python encrypt.py 3599 1759 | python decrypt.py 3599 2839