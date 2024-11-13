import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).

def keygen(lo, hi):
    # call function _primes to get the primes lis, from lo to hi(exclude)
    lis = _primes(lo, hi)

    # call function _choice, and ensure p and q get two different primes
    p = _choice(lis)
    q = _choice(lis)

    # while p is equal to q call _choice, keep random to chose the value from lis until we get a different value
    while p == q:
        q = _choice(lis)

    # set m and n by the given formular
    n = p * q
    m = (p - 1) * (q - 1)

    # call _primes create prime lis2 from 2 to m(exclude)
    lis2 = _primes(2, m)

    # while loop forever until break
    while True:

        # call _choice from lis2
        e = _choice(lis2)

        # if remainder is zero keep looping, until random e with non-zero remainder
        if m % e != 0:

            # meet condition non-zero remainder, break and step out the loop
            break

    # initial d
    d = 0

    # create for loop in range from 1 to m(exclude)
    for i in range(1, m):

        # create if e * i % m == 1 we keep the value (d = i) and break
        if e * i % m == 1:
            d = i
            break

    # return n, d, e in order as tuple
    return n, d, e

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):

    # return the value by using encrypt formular (x ** e) % n
    return (x ** e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # return the value by using decrypt formular (y ** d) % n
    return (y ** d) % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # create an empty list isprime (for checking)
    isprime = []

    # create for loop from 0 to hi(include)
    for i in range(hi + 1):

        # Append [True] to isprime
        isprime += [True]

    # set isprime[0] and isprime[1], 1 and 0 is not prime number
    isprime[0] = False
    isprime[1] = False

    # create a for loop in range from 2 to hi (include hi itself)
    for i in range(2, hi + 1):

        # create if isprime is True, we get in to check whether is prime num
        if isprime[i]:

            # create for loop in range 2 to hi // i (include), we mark all the value from 2 to hi // i + 1
            for j in range(2, hi // i + 1):

                # make all the value that can be multiple to False
                isprime[i * j] = False

    # create a list prime to store prime number that is True
    prime = []

    # create for loop from lo to hi(exclude) check isprime from lo to hi(exclude)
    for i in range(lo, hi):

        # if True, add the value to prime
        if isprime[i]:
            prime += [i]

    # return the list prime
    return prime


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # copy list a to list b
    b = a[:]

    # create a copy from 0 to k(exclude) elements, we name it as fk(first k)
    fk = b[:k]

    # shuffle the first k elements of fk which is the first k elements in list b
    stdrandom.shuffle(fk)

    # return list fk, because the problem only need the k item in the list that is shuffled
    return fk

# Returns a random item from the list a.
def _choice(a):
    # set l to length of list a
    l = len(a)

    # random the index of list a, we set the value to r
    r = stdrandom.uniformInt(0, l)

    # return int(a[r]) as a random value from a list
    return int(a[r])

# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))


if __name__ == "__main__":
    _main()
