import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).

def keygen(lo, hi):
    # call function _primes to get the primes lis, from lo to hi(exclude)
    lis = _primes(lo, hi)

    # call function sample, sample ensure p and q get two different primes
    p = _choice(lis)
    q = _choice(lis)
    while p == q:
        q = _choice(lis)

    # set m and n by the given formular
    n = p * q
    m = (p - 1) * (q - 1)

    lis2 = _primes(2, m)
    # call function _choice to get a random prime from lis2
    while True:
    # while m mod e is zero, random the value until the remainder is not 0
        e = _choice(lis2)
        if m % e != 0:
            break

    d = 0
    for i in range(1, m):
        if e * i % m == 1:
            d = i
            break


    return n, d, e

    # the idea for this problem is that keygen have to return the public and private key as tuple
    # picking prime numbers p and q and value of e
    # no calculation at that time, only get the value from it
    # the return value have to be a tuple(n, e, d), than it means that we only need to evaluate these three value
    # we need to pick the prime number p and q in [lo, hi)



# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # !!! issue occur Test Failed: local variable 'e' referenced before assignment
    # return the value by the given formular
    return (x ** e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # return the value by the given formular
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
    # create an empty list
    isprime = [True] * hi
    isprime[0] = False
    isprime[1] = False
    # create a for loop in range from lo to hi(exclude)
    for i in range(2, int(hi ** 0.5) + 1):
        if isprime[i]:
            # Mark all multiples of i as non-prime starting from i*i
            for j in range(i * i, hi, i):
                isprime[j] = False
    lis = []
    for i in range(lo, hi):
        if isprime[i]:
            lis += [i]

    # return the list
    return lis


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # !!!! issue occur
    # copy list a to list b
    b = a[:]

    # create a copy from 0 to k(exclude) elements, we name it as fk
    fk = b[:k]

    # shuffle the first k elements of fk which is the first k elements in list b
    stdrandom.shuffle(fk)

    # we assign the value that is shuffle in fk to the original b list first k element
    # notice that we need to apply the shuffle value to b[:k] because we only change it in fx


    # return list fk, because the problem only need the k item in the list
    return fk



# Returns a random item from the list a.
def _choice(a):
    # pass the test, no need to
    l = len(a)
    r = stdrandom.uniformInt(0, l)
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
