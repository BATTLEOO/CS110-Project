import stdio
import sys

# create k as int, mean the kth root of c
k = int(sys.argv[1])

# create c as float, find c's root. which c is from the user input
c = float(sys.argv[2])

# create EPSILON in float, means the decimal places that wanted by the user input
EPSILON = float(sys.argv[3])

#set t to c, we assign the value to t
t = c

# create a loop |1 - c / t^k| > EPSILON
# using abs to show it is a absolute value
while abs(1 - c / (t ** k)) > EPSILON:

# write the function that is provided
    t = t - (t**k - c) / (k * (t ** (k - 1)))

# write t to standard output
stdio.writeln(t)
