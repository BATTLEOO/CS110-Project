import rsa
import sys
import stdio

# Entry point.
def main():
    # private key: accept n and d as int argument
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # get the number of bits per character(width)
    width = rsa.bitLength(n)

    # use stdio.readAll to read the input from standard input, which will be the data from the encrypt.py.
    message = stdio.readAll()

    # set l as the length of message
    l = len(message)

    # create a for loop that is from  to l-1(exclude), and the step is width
    for i in range(0, l - 1, width):

        # we set s as a part of the list from i(previous stop point) to i + width (new stop point)
        s = message[i : i + width]

        # here we call rsa.bin2dec to convert binary to dec everytime
        y = rsa.bin2dec(s)

        # call rsa.decrypt to decrypt y to character
        decrypted = rsa.decrypt(y, n, d)

        # we obtained the value by using the built-in function chr()
        stdio.write(chr(decrypted))

if __name__ == "__main__":
    main()
