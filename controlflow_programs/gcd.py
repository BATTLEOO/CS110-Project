import stdio
import sys

# create p ,q as int argument
p, q = int(sys.argv[1]), int(sys.argv[2])

# create condition when p % q is zero print the remainder
while p % q != 0:

# set the remainder expression
    remainder = p % q

# everytime the new p will store the old q value
    p = q

# everytime the new p will store the remainder value from this time
    q = remainder

# After p % q is zero, means that gcd has been find, than write the q in standard output
# which is the last value that have been store in q (the previous remainder)
stdio.writeln(q)
