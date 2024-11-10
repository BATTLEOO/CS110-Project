import stdio
import sys

# create n as int
n = int(sys.argv[1])

# Set i to 2.
i = 2

# repeat if i is less than or equal to n / i
while i <= n / i:

# if i divides n, break because n is not a prime
    if n % i == 0:
        break

#  i = i + 1
    i += 1

if n % i != 0:
    # if  n is prime. Write True to standard output.
    stdio.writeln('True')
else:
    # if n is not a prime. Write False to standard output.
    stdio.writeln('False')