import stdio
import sys

# create n as int, n is the range of number you want to put in the fibonacci function
n = int(sys.argv[1])

# set a is zero and b is equal to b
a = 0
b = 1

# create a for loop in range 2 to n
for i in range(2, n + 1):

# store a value in a temp, we do not want to lose the value of a, we need to use it in the first repeat process
# everytime we update temp, from the previous a = b
    temp =a

# assign b value to a, we want to update a for the next repeat, we want to make sure this b value is from the previous repeat
# if we do not use temp to store a the a initial will be gone, we do not want that happen,
# the thing is we also want to update a, so first we store a to temp, then we store be to a.
    a = b

# b = temp + b, we update b value
# we use temp instead of a. temp begin with the initial but a do not
    b = temp + b

# write b in standard output
stdio.writeln(b)

#i   b   a      right b  +  temp    a = b (the b is from the previous time)
#2   1   1       1         0        1  ---------(this b is from the initial value we set)
#3   2   1       1         1        1  ---------(from here we begin to update)
#4   3   2       1         1        2  --------- ...
#5   5   3       3         2        3
#6   8   5       5         3        5
#7   13  8       8         5        8
#8   21  13      13        8        13
#9   34  21      21        13       21
#10  55  34      34        21       34