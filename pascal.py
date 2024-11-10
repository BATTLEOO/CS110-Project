import stdarray
import stdio
import sys

# create n as int argument
n = int(sys.argv[1])

# Create a list a of size n + 1 with all elements set to None, we stdarray.create1D())
a = stdarray.create1D(n + 1, None)

# create a for loop i in range from 0 to n + 1, (n include)
for i in range(0, n + 1):

# Set a[i] to a list of size i + 1 with all elements set to 1
    a[i] = stdarray.create1D(i + 1, 1)

# create a for loop i in range from 0 to n + 1, (n include)
for i in range(0, n + 1):

# create a inner for loop i in range from 1 to i, (i not include)
    for j in range(1, i):

# Set a[i][j] to a[i − 1][j − 1] + a[i − 1][j]
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

# create a for loop i in range from 0 to n + 1, (n include)
for i in range(0, n + 1):

# create a inner for loop j in range form 0 to i + 1, (i include)
    for j in range(0, i + 1):

# create an if statement, if j less than j we print a[i][j] in standard output with a space
        if j < i:
            stdio.write(str(a[i][j]) + " ")

# if not j < i, we create an else statement write a[i][j] in standard output in new line
        else:
            stdio.writeln(a[i][j])