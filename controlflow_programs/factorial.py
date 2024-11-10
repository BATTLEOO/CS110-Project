import stdio
import sys

# write n as int as the user input
n = int(sys.argv[1])

# initial result to 1
result = 1

# create a for loop to repeat from 1 to n
for i in range(1, n + 1):

# result = result * i, the result update everytime, the right result is from the previous updated result
    result *= i

# write result in standard output
stdio.writeln(result)
