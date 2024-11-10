import stdio

# read all strings from standard input into a list a
a = stdio.readAllStrings()

# set n to the length of a
n = len(a)

# use for loop, set i in range from 0 to n / 2, which n / 2 is not included
for i in range(0, (n // 2)):

# using swap method to exchange a[i] with a[n − i −1]
    temp = a[i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = temp

# use for loop, set i in range from 0 to n, n is not included
for i in range(0, n):

# in the inner, write if statement, if i is less than n - 1
#  if True, write a[i] with a space after in standard output
    if i < n - 1:
        stdio.write(a[i])
        stdio.write(" ")

# write else statement, write a[i] with a newline after in standard output
    else:
        stdio.writeln(a[i])

# NOTICE: In windows use ctrl Z to run the program instead of using D

