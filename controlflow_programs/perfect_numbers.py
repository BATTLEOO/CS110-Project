import stdio
import sys

# create n in int
n = int(sys.argv[1])

# write for in range in 2 to n
for i in range(2, n + 1):

# set total to zero
    total = 0

# write for j in range from 1 to i // 2
    for j in range(1, (i // 2) + 1):

# write if j mod i or i mod j have zero remainder
        if j % i == 0 or i % j == 0:

# if meet the if statement's condition, we add j to total
            total += j
# if total is equal to i
    if total == i:

# write i in standard output if condition is satisfy
        stdio.writeln(i)

