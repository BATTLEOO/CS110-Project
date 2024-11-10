import math
import stdio
import sys

# set n as int arguments, n is the number of input we want to have
n = int(sys.argv[1])

# create an empty list x, list x used to store the number we want to calculate
x = []

# use for loop, set the range from 0 to n, n is not included
for i in range(0, n):

# the user input should be read here
# set a value to store the user input to float
    value = stdio.readFloat()

# Append the value one by one from user input
    x += [value]



# create a y list that is empty
y = []

# need another for loop that is the same idea form x
for i in range(0, n):

# set the value 2 to read the user input
    value2 = stdio.readFloat()

# Append the value on by one from the user input

    y += [value2]

# set distance to 0.0
distance = 0.0

# set range from i to n, n not include
for i in range(0, n):

# Increment distance by (x[i] − y[i]) ** 2
    distance = distance + (x[i] - y[i]) ** 2.0

# Write distance in sqrt in standard output
stdio.writeln(math.sqrt(distance))

