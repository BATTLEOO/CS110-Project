import stdarray
import stdio
import sys

# Create m and n as int
m = int(sys.argv[1])
n = int(sys.argv[2])

# Create an m * n list, and set the value to None
a = stdarray.create2D(m, n, None)

# set for loop i in range from 0 to m(not include), this is row
for i in range(0, m):

# set for loop j in range from 0 to n(not include), this is column
    for j in range(0, n):

# Set a[i][j] to a float read from standard input, I use value1 to store the input
        value1 = stdio.readFloat()

# assign value1 to a[i][j]
        a[i][j] = value1

# Create an n ×m list c, elements to None
c = stdarray.create2D(n, m, None)

# Create for loop i in range from 0 to n(not include)
for i in range(0, n):

# Create for loop j in range from 0 to m(not include)
    for j in range(0, m):

# Assign a[j][i] to c[i][j]
        c[i][j] = a[j][i]

# Create for loop i in range from 0 to n(not include)
for i in range(0, n):

# Create for loop j in range from 0 to m(not include)
    for j in range(0,m):

# write if statement If j < m−1, write c[i][j] with a space after in standard output
        if j < m - 1:
            stdio.write(str(c[i][j]) + " ")

# write else statement, write c[i][j] with a newline after in standard output
        else:
            stdio.writeln(c[i][j])
