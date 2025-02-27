import stdio
import sys

# create n as int
n = int(sys.argv[1])

# Set count (number of primes <= n) to 0
count = 0

for i in range(0, n + 1):
    # for each i from 2 to n

    # Set j (potential divisor of i) to 2.
    j = 2

    while j <= i / j:
        # As long as j is less than or equal to i / j

        if i % j == 0:
            # If j divides i, break (i is not a prime).
            break

        # Increment j by 1.
        j += 1

    # If you got here by exhausting the while loop, i is a prime, so increment count by 1.
    if i % j != 0:
        count += 1

# Write count to standard output.
stdio.writeln(str(count))
