import stdio
import sys

# create n as int, n is the range of number that you want to have
n = int(sys.argv[1])

# create k as int, k is the power you want to have
k = int(sys.argv[2])

# initial the value total to 0
total = 0

# create a for loop in range from 1 to the user input n
for i in range(1, n + 1):

# this line means total = total + i^k, everytime the total on the right update, and add the new i^k, until to the n
    total += i ** k

# write total in standard output
stdio.writeln(total)
